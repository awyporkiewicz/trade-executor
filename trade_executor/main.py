import asyncio

from trade import Trade
from ws_client import ws_run
from helpers.init_db import create_connection
from helpers.config import schema_path, db_file, args


# the app entry: python main.py --q 500 -p 240.50
def main():
    connection = create_connection(schema_path=schema_path, db_file=db_file)
    trade = Trade(
        quantity=args.quantity,
        min_price=args.price,
        db_file=db_file,
        connection=connection,
    )
    asyncio.run(ws_run(trade=trade))
    connection.close()
    print("Transaction finished")


if __name__ == "__main__":
    main()
