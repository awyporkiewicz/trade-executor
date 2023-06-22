from decimal import Decimal
from dataclasses import dataclass


@dataclass
class Rate:
    update_id: int
    symbol: str
    bid_price: Decimal
    bid_qty: Decimal
    ask_price: Decimal
    ask_qty: Decimal
