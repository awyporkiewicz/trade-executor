import asyncio

from helpers.config import args
from helpers.init_db import create_connection
from trade_executor.trade import Trade
from trade_executor.ws_client import ws_run


def main() -> None:
    connection = create_connection()
    trade = Trade(args.exchange, args.price, args.quantity)
    with connection:
        asyncio.run(ws_run(trade, args.symbol, connection))


if __name__ == "__main__":
    main()
