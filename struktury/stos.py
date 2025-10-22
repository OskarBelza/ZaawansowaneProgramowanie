from typing import Any, List


class Stos:
    def __init__(self) -> None:
        self._items: List[Any] = []

    def push(self, element: Any) -> None:
        self._items.append(element)

    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0
