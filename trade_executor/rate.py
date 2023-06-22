from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Rate:
    update_id: int
    symbol: str
    bid_price: Decimal
    bid_qty: Decimal
    ask_price: Decimal
    ask_qty: Decimal
