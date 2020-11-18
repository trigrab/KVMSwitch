#!/usr/bin/env python3

import asyncio
import argparse
import json
import websockets
from config import config

class ESPDashClient:
    cards = []
    uri = "ws://{hostname}:80/dashws"

    def main(self):
        self.uri = self.uri.format(hostname=config.hostname)
        answer = asyncio.get_event_loop().run_until_complete(self.get_layout())
        self.parse_answer(answer)
        card = self.find_card(self.name)
        if card is not None:
            message = {"command": "buttonClicked",
                           "id": str(card["id"]),
                           "value": bool(card["value"])} 
            asyncio.get_event_loop().run_until_complete(self.post(message))
            print(f"message sent: {message}")

    def find_card(self, name):
        for card in self.cards:
            if name.lower() in card["name"].lower():
                return card

    async def get_layout(self):
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
    parser.add_argument("card", help="name of the card you want to click (partial suffices)")
    args = parser.parse_args()

    kvm = ESPDashClient()
    kvm.name = args.card
    kvm.main()
