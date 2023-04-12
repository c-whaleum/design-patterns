from .subscribers import *
from .publishers import *
from .events import *

def simulate_market(econ: EconPublisher, stock: StockPublisher):
    econ.new_inflation_data(1.2)
    econ.new_inflation_data(1.3)
    stock.new_stock_data(100)
    stock.new_stock_data(110)
    econ.new_inflation_data(1.4)
    econ.new_housing_data(1.2)


def run_oberver():
    econ = EconPublisher()
    stock = StockPublisher()
    jpm = BankSubscriber('JPM')
    bac = BankSubscriber('BAC')
    shitadel = HedgeFundSubscriber('Shitadel')
    pointblank72 = HedgeFundSubscriber('PointBlank72')
    usausausa = GovernmentSubscriber('USAUSAUSA')
    bad_trader = TraderSubscriber('Bad Trader')
    
    # Subscribe to econ events
    econ.add_subscriber(Events.INFLATION_CHANGED, jpm.update)
    econ.add_subscriber(Events.HOUSE_PRICE_CHANGED, jpm.update)
    econ.add_subscriber(Events.INFLATION_CHANGED, bac.update)
    econ.add_subscriber(Events.HOUSE_PRICE_CHANGED, bac.update)
    econ.add_subscriber(Events.INFLATION_CHANGED, shitadel.update)
    econ.add_subscriber(Events.INFLATION_CHANGED, pointblank72.update)
    
    # Subscribe to stock events
    stock.add_subscriber(Events.STOCK_PRICE_CHANGED, jpm.update)
    stock.add_subscriber(Events.STOCK_PRICE_CHANGED, bac.update)
    stock.add_subscriber(Events.STOCK_PRICE_CHANGED, shitadel.update)
    stock.add_subscriber(Events.STOCK_PRICE_CHANGED, pointblank72.update)
    stock.add_subscriber(Events.STOCK_PRICE_CHANGED, usausausa.update)
    stock.add_subscriber(Events.STOCK_PRICE_CHANGED, bad_trader.update)
    
    simulate_market(econ, stock)