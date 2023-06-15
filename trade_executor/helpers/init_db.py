import sqlite3
import decimal

D = decimal.Decimal


def adapt_decimal(d):
    return str(d)


def convert_decimal(s):
    return decimal.Decimal(s)


def create_connection(schema_path: str, db_file: str):
    with open(schema_path, "r") as sql_file:
        sql_script = sql_file.read()
    sqlite3.register_adapter(decimal.Decimal, adapt_decimal)
    sqlite3.register_converter("DECTEXT", convert_decimal)

    conn = sqlite3.connect(db_file, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.isolation_level = None
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    return conn
