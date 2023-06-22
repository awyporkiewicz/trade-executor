import sqlite3
from unittest.mock import Mock, patch

from trade_executor.helpers.logger import logger
from trade_executor.process import Process
from trade_executor.trade import Trade
from trade_executor.ws_client import process_data


def test_process_data() -> None:
    mock_connection = Mock(spec=sqlite3.Connection)
    response = (
        '{"u": 8570197034, "s": "BNBUSDT", "b": "245.80000000", '
        '"B": "336.83000000", "a": "245.90000000", "A": "267.71900000"}'
    )
    trade = Trade(exchange="bid", specified_price=239, quantity=100)

    with patch(
        "trade_executor.ws_client.save_trading_process"
    ) as mock_save_trading_process:
        process_data(response, trade, mock_connection)
        expected_process = Process(
            update_id=8570197034,
            symbol="BNBUSDT",
            exchange="bid",
            price="245.80000000",
            selected_qty="100",
        )
        mock_save_trading_process.assert_called_once_with(
            expected_process, mock_connection, logger
        )
