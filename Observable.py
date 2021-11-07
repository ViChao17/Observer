class ObserverInterface:
    def update(self, obs, arg):
        pass


class Observable:

    def __init__(self):
        self.observers: list[ObserverInterface] = []
        self.changed: bool = False

    def register(self, o: ObserverInterface):
        self.observers.append(o)

    def remove(self, o: ObserverInterface):
        self.observers.remove(o)

    def notify(self, arg=None):
        if self.changed:
            for o in self.observers:
                o.update(self, arg)
            self.changed = False

    def set_changed(self):
        self.changed = True


class Observer(ObserverInterface):
    def update(self, obs: Observable, arg):
        pass
