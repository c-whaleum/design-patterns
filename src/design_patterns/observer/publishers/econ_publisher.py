from .event_manager import EventManager
from design_patterns.observer.events import Events

class EconPublisher():
    def __init__(self):
        self._event_manager = EventManager()
        self.inflation_data = []
        self.housing_data = []
       
    def new_inflation_data(self, data):
        self.inflation_data.append(data)
        self._event_manager.notify(Events.INFLATION_CHANGED, data)
    
    def new_housing_data(self, data):
        self.housing_data.append(data)
        self._event_manager.notify(Events.HOUSE_PRICE_CHANGED, data)
    
    def add_subscriber(self, event, callback):
        self._event_manager.subscribe(event, callback)
    
    def remove_subscriber(self, event, callback):
        self._event_manager.unsubscribe(event, callback)