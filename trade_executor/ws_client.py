import json
import sqlite3
from decimal import Decimal

import websockets
from trade_executor.helpers.logger import logger
from trade_executor.process import save_trading_process
from trade_executor.rate import Rate
from trade_executor.trade import Trade


async def ws_run(trade: Trade, symbol: str, connection: sqlite3.Connection) -> None:
    async with websockets.connect(
        f"wss://stream.binance.com:9443/ws/{symbol}@bookTicker"
    ) as websocket:
        while not trade.complete:
            response = await websocket.recv()
            process_data(response, trade, connection)
    logger.info("Trading closed.")


def process_data(response: str, trade: Trade, connection: sqlite3.Connection) -> None:
    rate = json.loads(
        response,
        object_hook=lambda res: Rate(
            update_id=res["u"],
            symbol=res["s"],
            bid_price=Decimal(res["b"]),
            bid_qty=Decimal(res["B"]),
            ask_price=Decimal(res["a"]),
            ask_qty=Decimal(res["A"]),
        ),
    )
    if trade.should_trade(rate):
        process = trade.prepare_trade_process(rate)
        save_trading_process(process, connection, logger)
