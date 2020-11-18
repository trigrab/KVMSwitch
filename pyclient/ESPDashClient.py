#!/usr/bin/env python3

import asyncio
import argparse
import json
import re
import websockets
from config import Config


class ESPDashClient:
    cards = []
    uri = "ws://{hostname}:{port}/dashws"

    def __init__(self):
        self.uri = self.uri.format(hostname=Config.hostname, port=Config.port)

    def click_card(self, query):
        """
        click first card that matches query
        :param query: string to query the card name, spaces equal regex ".*"
        :return: None
        """
        self.get_layout()
        card = self.find_cards(query)[0]
        if card is not None:
            message = {"command": "buttonClicked",
                       "id": str(card["id"]),
                       "value": bool(card["value"])}
            asyncio.get_event_loop().run_until_complete(self.post(message))
            print(f"clicked card: {card['name']}")

    def find_cards(self, query):
        if query is None:
            return self.cards

        regex = re.compile(query.replace("*", ".*").replace(" ", ".*"),
                           re.IGNORECASE | re.DOTALL)

        def filter_(x):
            return regex.search(x) is not None

        result = [c for c in self.cards if filter_(c["name"])]
        return result

    def get_layout(self):
        answer = asyncio.get_event_loop().run_until_complete(self._get_layout())
        self.parse_answer(answer)

    async def _get_layout(self):
        async with websockets.connect(self.uri) as websocket:
            message = {"command": "getLayout"}

            await websocket.send(json.dumps(message))

            answer = await websocket.recv()
            return json.loads(answer)

    async def post(self, message):
        async with websockets.connect(self.uri) as websocket:
            await websocket.send(json.dumps(message))

    def parse_answer(self, answer):
        if answer["command"] == "updateLayout":
            self.cards = answer["cards"]
        else:
            print(json.dumps(answer, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("card", help="name of the card you want to click (partial suffices)",
                        nargs="?")
    args = parser.parse_args()

    dash_client = ESPDashClient()
    dash_client.get_layout()
    dash_client.click_card(args.card)
