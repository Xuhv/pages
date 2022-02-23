from typing import Callable

def singleton(cls, *args, **kw):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

class Event:
    def __init__(self, name: str, *params) -> None:
        self.name = name
        self.params = params

@singleton
class EventBus:
    def __init__(self) -> None:
        self.subscribers: dict[str, list[Subscriber]] = {}

    def publish(self, event: Event) -> None:
        if event.name not in self.subscribers:
            return

        for subscriber in self.subscribers[event.name]:
            subscriber.notify(event)

class Publisher:
    def __init__(self) -> None:
        self.bus: EventBus = EventBus()
    
    def publish(self, event: str, *params) -> None:
        self.bus.publish(Event(event, *params))

class Subscriber:
    def __init__(self) -> None:
        self.bus = EventBus()
        self.subscriptions: dict[str, Callable] = {}

    def notify(self, event: Event) -> None:
        self.subscriptions[event.name](*event.params)

    def subscribe(self, event: str, handler: Callable) -> None:
        self.subscriptions[event] = handler
        if not event in self.bus.subscribers:
            self.bus.subscribers[event] = []
        self.bus.subscribers[event].append(self)

    def unsubscribe(self, event: str) -> None:
        self.subscriptions.pop(event)
        self.bus.subscribers[event].remove(self)

a = Publisher()
b = Subscriber()

b.subscribe('test', lambda x: print(x))
a.publish('test', 'hello world')
