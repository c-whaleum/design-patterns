from enum import Enum

class Events(Enum):
    STOCK_PRICE_CHANGED = 1
    STOCK_LISTED = 2
    STOCK_DELISTED = 3
    INFLATION_CHANGED = 4
    HOUSE_PRICE_CHANGED = 5