from datetime import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Transction:
    id: int
    name: str
    symbol: str
    type: int
    amount: int
    time_transacted: datetime
    time_created: datetime
    price_purchased_at: float
    no_of_coins: float


def format_db_row_to_transaction(row):
    return Transction(
        id=row[0],
        name=row[1],
        symbol=row[2],
        type=row[3],
        amount=row[4],
        time_transacted=row[5],
        time_created=row[6],
        price_purchased_at=row[7],
        no_of_coins=row[8],
    )
