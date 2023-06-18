from decimal import Decimal


class Offer:
    def __init__(self, u: int, s: str, b: str, B: str, a: str, A: str):
        self.update_id = u
        self.symbol = s
        self.bid_price = Decimal(b)
        self.bid_qty = Decimal(B)
        self.ask_price = Decimal(a)
        self.ask_qty = Decimal(A)
