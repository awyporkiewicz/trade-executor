import logging
import sqlite3
from dataclasses import dataclass


@dataclass
class Process:
    update_id: int
    symbol: str
    exchange: str
    price: str
    selected_qty: str


def save_trading_process(
    process: Process, connection: sqlite3.Connection, logger: logging.Logger
) -> None:
    try:
        values = (
            process.update_id,
            process.symbol,
            process.exchange,
            process.price,
            process.selected_qty,
        )
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO trade(update_id, symbol, exchange, price, quantity) VALUES(?, ?, ?, ?, ?)",
            values,
        )
        connection.commit()
        logger.info(f"Trade accepted: {process}")
    except sqlite3.Error as err:
        logger.error("An error occurred while executing the connection: " + str(err))
