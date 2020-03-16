from typing import List


class Subscriber(object):
    def __init__(self):
        self.msg: str = ""


class Observer(object):
    def __init__(self):
        self.subscribers: List[Subscriber] = []

    def update(self, msg: str):
        for subscriber in self.subscribers:
            subscriber.msg = msg

    def register(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)

    def unregister(self, subscriber: Subscriber):
        self.subscribers.remove(subscriber)


class Subscription(object):
    def __init__(self):
        self.observers: List[Observer] = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, msg):
        for observer in self.observers:
            observer.update(msg)


if __name__ == "__main__":
    obs = Observer()
    s1 = Subscriber()
    s2 = Subscriber()
    s3 = Subscriber()
    obs.register(s1)
    obs.register(s2)
    obs.register(s3)
    sub = Subscription()
    sub.attach(obs)

    sub.notify("Hi")

    for s in obs.subscribers:
        print(s.msg)
