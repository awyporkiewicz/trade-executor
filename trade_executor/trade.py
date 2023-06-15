import sqlite3
from decimal import Decimal

from offer import Offer
from helpers.init_db import adapt_decimal


class Trade:
    def __init__(
        self,
        quantity: float,
        min_price: float,
        db_file: str,
        connection: sqlite3.Connection,
    ):
        self.quantity = Decimal(quantity)
        self.min_price = min_price
        self.db_file = db_file
        self.connection = connection
        self.complete = False

    def execute_trade(self, offer: Offer):
        if offer.bid_price >= self.min_price:
            bid_quantity = self._set_quantity(bid_quantity=offer.bid_qty)

            bid_offer = (
                offer.update_id,
                offer.symbol,
                adapt_decimal(offer.bid_price),
                adapt_decimal(bid_quantity),
            )
            self._save_trade(bid_offer=bid_offer)

    def _set_quantity(self, bid_quantity: Decimal):
        if bid_quantity < self.quantity:
            self.quantity = self.quantity - bid_quantity
        else:
            bid_quantity = self.quantity
            self.quantity = 0
            self.complete = True
        return bid_quantity

    def _save_trade(self, bid_offer: tuple):
        try:
            cursor = self.connection.cursor()
            cursor.execute("begin")
            cursor.execute(
                f"INSERT INTO trade(update_id, symbol, price, quantity) VALUES {bid_offer}"
            )
            cursor.execute("commit")
            print(f"Transaction accepted: {bid_offer}")
        except self.connection.Error as e:
            print(e)
            cursor.execute("rollback")
