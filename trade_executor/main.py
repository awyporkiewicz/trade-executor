import asyncio

from helpers.config import args, db_file, schema_path
from helpers.init_db import create_connection
from trade import Trade
from ws_client import ws_run


# the app entry: python main.py --q 500 -p 240.50
def main():
    connection = create_connection(schema_path=schema_path, db_file=db_file)
    trade = Trade(
        quantity=args.quantity,
        min_price=args.price,
        db_file=db_file,
        connection=connection,
    )
    with connection:
        asyncio.run(ws_run(trade))
    # connection.close()
    print("Transaction finished")


if __name__ == "__main__":
    main()
