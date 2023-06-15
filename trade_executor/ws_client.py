import json

import websockets
from offer import Offer
from trade import Trade


async def ws_run(trade: Trade):
    async with websockets.connect(
        "wss://stream.binance.com:9443/ws/bnbusdt@bookTicker"
    ) as websocket:
        while not trade.complete:
            response = await websocket.recv()
            print(response)
            offer = json.loads(response, object_hook=lambda x: Offer(**x))
            trade.execute_trade(offer=offer)
