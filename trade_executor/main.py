import asyncio

from helpers.config import args
from helpers.init_db import create_connection
from trade_executor.trade import Trade
from ws_client import ws_run


def main():
    connection = create_connection()
    trade = Trade(args.quantity, args.price, connection)
    with connection:
        asyncio.run(ws_run(trade, args.symbol, args.exchange))
    print("Transaction finished.")


if __name__ == "__main__":
    main()
