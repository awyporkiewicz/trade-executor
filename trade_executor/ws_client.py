import json

import websockets
from trade_executor.offer import Offer
from trade_executor.trade import Trade


async def ws_run(trade: Trade, symbol: str, exchange: str):
    async with websockets.connect(
        f"wss://stream.binance.com:9443/ws/{symbol}@bookTicker"
    ) as websocket:
        while not trade.complete:
            response = await websocket.recv()
            rates = json.loads(response, object_hook=lambda x: Offer(**x))
            offer = (
                trade.analyse_bid_offer(rates)
                if exchange == "bid"
                else trade.analyse_ask_offer(rates)
            )
            if offer:
                trade.save_trade(offer)
