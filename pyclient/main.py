#!/usr/bin/env python3

import asyncio
import argparse
import json
import websockets


class KVMSwitchWSClient:
    cards = []
    name = "Laptop"
    uri = "ws://192.168.42.90:80/dashws"

    def main(self):
        answer = asyncio.get_event_loop().run_until_complete(self.hello())
        self.parse_answer(answer)
        print(self.name)
        card = self.find_card(self.name)
        if card is not None:
            asyncio.get_event_loop().run_until_complete(
                self.post({"command": "buttonClicked",
                           "id": str(card["id"]),
                           "value": bool(card["value"])}))

    def find_card(self, name):
        for card in self.cards:
            if name.lower() in card["name"].lower():
                return card

    async def hello(self):
        async with websockets.connect(self.uri) as websocket:
            message = {"command": "getLayout"}

            await websocket.send(json.dumps(message))
            print(f"> {message}")

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
                        nargs='?', default="Laptop")
    args = parser.parse_args()

    kvm = KVMSwitchWSClient()
    kvm.name = args.card
    kvm.main()
