import sqlite3
from decimal import Decimal

from trade_executor.offer import Offer


class Trade:
    def __init__(
        self,
        quantity: float,
        specified_price: float,
        connection: sqlite3.Connection,
    ):
        self.quantity = Decimal(quantity)
        self.specified_price = specified_price
        self.connection = connection
        self.complete = False

    def analyse_bid_offer(self, offer: Offer):
        if offer.bid_price < self.specified_price:
            return None
        bid_quantity = self._set_quantity(offer.bid_qty)
        return (
            offer.update_id,
            offer.symbol,
            str(offer.bid_price),
            str(bid_quantity),
        )

    def analyse_ask_offer(self, offer: Offer):
        if offer.ask_price < self.specified_price:
            return None
        ask_quantity = self._set_quantity(offer.ask_qty)
        return (
            offer.update_id,
            offer.symbol,
            str(offer.ask_price),
            str(ask_quantity),
        )

    def save_trade(self, bid_offer: tuple):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO trade(update_id, symbol, price, quantity) VALUES(?, ?, ?, ?)",
                bid_offer,
            )
            self.connection.commit()
            print(f"Trade accepted: {bid_offer}")
        except self.connection.Error as e:
            print(e)

    def _set_quantity(self, offer_quantity: Decimal):
        if offer_quantity < self.quantity:
            self.quantity = self.quantity - offer_quantity
        else:
            offer_quantity = self.quantity
            self.quantity = Decimal("0")
            self.complete = True
        return offer_quantity
