import decimal
import os
import sqlite3


def create_connection() -> sqlite3.Connection:
    path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        os.path.join("data/"),
    )
    with open(path + "schema.sql", "r") as sql_file:
        sql_script = sql_file.read()
    sqlite3.register_adapter(decimal.Decimal, lambda d: str(d))
    sqlite3.register_converter("DECTEXT", lambda s: decimal.Decimal(s))

    conn = sqlite3.connect(path + "trade.sqlite3", detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    return conn
