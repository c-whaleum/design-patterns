from .event_manager import EventManager
from design_patterns.observer.events import Events

class StockPublisher():
    def __init__(self):
        self._event_manager = EventManager()
        self.stock_data = []
       
    def new_stock_data(self, data):
        self.stock_data.append(data)
        self._event_manager.notify(Events.INFLATION_CHANGED, data)
    
    def add_subscriber(self, event, callback):
        self._event_manager.subscribe(event, callback)
    
    def remove_subscriber(self, event, callback):
        self._event_manager.unsubscribe(event, callback)