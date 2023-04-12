from collections import defaultdict

class EventManager():
    def __init__(self):
        self._subscribers = defaultdict(list)
    
    def subscribe(self, event, callback):
        self._subscribers[event].append(callback)
    
    def unsubscribe(self, event, callback):
        self._subscribers[event].remove(callback)
    
    def notify(self, event, *args, **kwargs):
        for callback in self._subscribers[event]:
            callback(*args, **kwargs)
        