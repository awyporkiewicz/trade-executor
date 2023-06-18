from unittest.mock import Mock
import pytest

from trade_executor.offer import Offer
from trade_executor.trade import Trade


@pytest.fixture
def offer():
    return Offer(
        u=8547806975,
        s="BNBUSDT",
        b="239.10000000",
        B="224.17000000",
        a="239.20000000",
        A="67.42400000",
    )


@pytest.fixture
def mock_connection():
    mock = Mock()
    return mock


def test_analyse_bid_offer_partial_amount(offer, mock_connection):
    trade = Trade(
        quantity=100,
        specified_price=239,
        connection=mock_connection,
    )
    assert trade.analyse_bid_offer(offer) == (
        8547806975,
        "BNBUSDT",
        "239.10000000",
        "100",
    )


def test_analyse_bid_offer_below_price(offer, mock_connection):
    trade = Trade(
        quantity=100,
        specified_price=250,
        connection=mock_connection,
    )
    assert trade.analyse_bid_offer(offer) is None


def test_analyse_ask_offer_full_amount(offer, mock_connection):
    trade = Trade(
        quantity=100,
        specified_price=239,
        connection=mock_connection,
    )
    assert trade.analyse_ask_offer(offer) == (
        8547806975,
        "BNBUSDT",
        "239.20000000",
        "67.42400000",
    )


def test_analyse_ask_offer_below_price(offer, mock_connection):
    trade = Trade(
        quantity=100,
        specified_price=250,
        connection=mock_connection,
    )
    assert trade.analyse_ask_offer(offer) is None
