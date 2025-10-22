from typing import Any, List


class Kolejka:
    def __init__(self) -> None:
        self._items: List[Any] = []

    def enqueue(self, element: Any) -> None:
        self._items.append(element)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._items.pop(0)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)
