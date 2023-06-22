from decimal import Decimal

from trade_executor.process import Process
from trade_executor.rate import Rate


class Trade:
    def __init__(
        self,
        exchange: str,
        specified_price: float,
        quantity: float,
    ):
        self.complete = False
        self.exchange = exchange
        self.specified_price = Decimal(specified_price)
        self.quantity = Decimal(quantity)

    def should_trade(self, rate: Rate) -> bool:
        if (self.exchange == "bid" and rate.bid_price >= self.specified_price) or (
            self.exchange == "ask" and rate.ask_price >= self.specified_price
        ):
            return True
        return False

    def prepare_trade_process(self, rate: Rate) -> Process:
        return (
            Process(
                update_id=rate.update_id,
                symbol=rate.symbol,
                exchange=self.exchange,
                price=str(rate.bid_price),
                selected_qty=str(self._set_trade_quantity(rate.bid_qty)),
            )
            if self.exchange == "bid"
            else Process(
                update_id=rate.update_id,
                symbol=rate.symbol,
                exchange=self.exchange,
                price=str(rate.ask_price),
                selected_qty=str(self._set_trade_quantity(rate.ask_qty)),
            )
        )

    def _set_trade_quantity(self, limit_quantity: Decimal) -> Decimal:
        if limit_quantity < self.quantity:
            self.quantity -= limit_quantity
        else:
            self.complete = True
            limit_quantity = self.quantity
            self.quantity = Decimal("0")
        return limit_quantity
