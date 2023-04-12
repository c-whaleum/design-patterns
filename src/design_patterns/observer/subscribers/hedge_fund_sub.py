from .subscriber import Subscriber
class HedgeFundSubscriber(Subscriber):

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} received message: {message}')

    def __str__(self):
        return self.name