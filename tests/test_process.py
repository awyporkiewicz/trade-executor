import logging
import sqlite3
from unittest.mock import MagicMock

from trade_executor.process import Process, save_trading_process


def test_save_trading_process() -> None:
    mock_connection = MagicMock(spec=sqlite3.Connection)
    mock_logger = MagicMock(spec=logging.Logger)
    process = Process(
        update_id=25618846079,
        symbol="ETHUSDT",
        exchange="ask",
        price="1898.15000000",
        selected_qty="33.48960000",
    )
    save_trading_process(process, mock_connection, mock_logger)

    mock_connection.cursor().execute.assert_called_once_with(
        "INSERT INTO trade(update_id, symbol, exchange, price, quantity) VALUES(?, ?, ?, ?, ?)",
        (
            process.update_id,
            process.symbol,
            process.exchange,
            process.price,
            process.selected_qty,
        ),
    )
    mock_connection.commit.assert_called_once()


def test_save_trading_process_error() -> None:
    mock_connection = MagicMock(spec=sqlite3.Connection)
    mock_logger = MagicMock(spec=logging.Logger)
    process = Process(
        update_id=25618846079,
        symbol="ETHUSDT",
        exchange="ask",
        price="1898.15000000",
        selected_qty="33.48960000",
    )
    mock_connection.cursor.side_effect = sqlite3.Error("Connection error")
    save_trading_process(process, mock_connection, mock_logger)
    expected_error_message = (
        "An error occurred while executing the connection: Connection error"
    )
    mock_logger.error.assert_called_once_with(expected_error_message)
