from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Observer import Observer


class Observable:

    def __init__(self):
        self.observers: list[Observer] = []
        self.changed: bool = False

    def register(self, o: Observer):
        self.observers.append(o)

    def remove(self, o: Observer):
        self.observers.remove(o)

    def notify(self, arg=None):
        if self.changed:
            for o in self.observers:
                o.update(self, arg)
            self.changed = False

    def set_changed(self):
        self.changed = True
