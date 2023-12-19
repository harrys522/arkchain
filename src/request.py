import sys
import websockets
import asyncio
import json
from datetime import datetime
import argparse

# connects to endpoint ENDPOINT


async def main():
    ENDPOINT = 'wss://ws.yobp0j.tech.openmesh.network'
    parser = argparse.ArgumentParser()

    parser.add_argument('--channel', help='channel to subscribe to')
    parser.add_argument('--exchange', help='exchange to subscribe to')
    parser.add_argument('--symbol', help='symbol to subscribe to')
    parser.add_argument('--frequency', help='frequency of messages')

    args = parser.parse_args().__dict__

    new_args = args.copy()
    for key in args:
        if args[key] is None:
            del new_args[key]

    args = new_args
    async with websockets.connect(ENDPOINT) as websocket:
        msg = {
            'action': 'subscribe',
            **args
        }
        print(json.dumps(msg, indent=4))
        await websocket.send(json.dumps(msg))
        async for message in websocket:
            msg = json.loads(message)
            print(json.dumps(msg, indent=4, default=str))

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")