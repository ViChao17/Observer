from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Observable import Observable


class Observer:
    def update(self, obs: Observable, arg):
        pass

