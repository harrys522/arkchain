import sys
import websockets
import asyncio
import json

#connects to endpoint ENDPOINT
async def main():
    ENDPOINT = 'wss://ws.shared.projectx.network'
    async with websockets.connect(ENDPOINT) as websocket:
        await websocket.send('{"action": "subscribe", "Real-Time Streaming, Crypto Exchanges, L2 Trades, WebSocket" : "%s", "channel": "%s", "symbol": "%s"}' % (sys.argv[1], sys.argv[2], sys.argv[3]))
    async for message in websocket:
        msg = json.loads(message)
    print(json.dumps(msg, indent=4, default=str))

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
