from decimal import Decimal

import pytest
from trade_executor.process import Process
from trade_executor.rate import Rate
from trade_executor.trade import Trade


@pytest.fixture
def rate() -> Rate:
    return Rate(
        update_id=8547806975,
        symbol="BNBUSDT",
        bid_price=Decimal("239.10000000"),
        bid_qty=Decimal("224.17000000"),
        ask_price=Decimal("239.20000000"),
        ask_qty=Decimal("67.42400000"),
    )


def test_prepare_trade_process(rate: Rate) -> None:
    test_trade = Trade(
        exchange="ask",
        specified_price=239,
        quantity=100,
    )
    assert test_trade.prepare_trade_process(rate) == Process(
        update_id=8547806975,
        symbol="BNBUSDT",
        exchange="ask",
        price="239.20000000",
        selected_qty="67.42400000",
    )
    assert test_trade.complete is False


def test_prepare_trade_process_complete(rate: Rate) -> None:
    test_trade = Trade(
        exchange="bid",
        specified_price=239,
        quantity=100,
    )
    assert test_trade.prepare_trade_process(rate) == (
        Process(
            update_id=8547806975,
            symbol="BNBUSDT",
            exchange="bid",
            price="239.10000000",
            selected_qty="100",
        )
    )
    assert test_trade.quantity == Decimal("0")
    assert test_trade.complete is True


@pytest.mark.parametrize(
    "test_trade,expected",
    [
        (
            Trade(
                exchange="bid",
                specified_price=240,
                quantity=100,
            ),
            False,
        ),
        (
            Trade(
                exchange="ask",
                specified_price=239.20000000,
                quantity=100,
            ),
            True,
        ),
    ],
)
def test_should_trade(rate: Rate, test_trade: Trade, expected: Process) -> None:
    assert test_trade.should_trade(rate) == expected
