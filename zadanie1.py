from datetime import datetime
from typing import Optional


class ActionNode:
    """
    Węzeł reprezentujący pojedynczą operację w historii.
    """

    def __init__(self, text: str):
        self.text: str = text
        self.timestamp: datetime = datetime.now()
        self.prev: Optional['ActionNode'] = None
        self.next: Optional['ActionNode'] = None

    def __repr__(self) -> str:
        return f"Action(time={self.timestamp.strftime('%H:%M:%S')}, text='{self.text}')"


class TextHistory:
    """
    Klasa zarządzająca historię zmian (lista dwukierunkowa).
    """

    def __init__(self):
        self.current: Optional[ActionNode] = None

    def add_action(self, text: str) -> None:
        """
        Dodaje nową operację do historii.
        """
        new_node = ActionNode(text)

        if self.current is None:
            self.current = new_node
            return

        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node

    def undo(self) -> Optional[str]:
        """
        Cofa ostatnią operację. Przesuwa wskaźnik current wstecz.
        """
        if self.current is None:
            print("Błąd: Historia jest pusta.")
            return None

        if self.current.prev is None:
            print("Info: Jesteś na początku historii, nie można cofnąć dalej.")
            return None

        self.current = self.current.prev
        return self.current.text

    def redo(self) -> Optional[str]:
        """
        Ponawia cofniętą operację. Przesuwa wskaźnik current w przód.
        """
        if self.current is None:
            return None

        if self.current.next is None:
            print("Info: Jesteś na końcu historii, nie ma nic do ponowienia.")
            return None

        self.current = self.current.next
        return self.current.text

    def show_current_state(self) -> None:
        if self.current:
            print(f"CURRENT: {self.current}")
        else:
            print("CURRENT: Pusty stan (lub początek historii)")


# --- Testowanie ---
if __name__ == "__main__":
    history = TextHistory()

    history.add_action("Wersja 1")
    history.add_action("Wersja 2")
    history.add_action("Wersja 3")
    history.show_current_state()

    history.undo()
    history.undo()
    history.undo()
    history.show_current_state()

    history.redo()
    history.show_current_state()

    history.add_action("Wersja 2b (Alternatywna)")

    history.show_current_state()
    history.redo()
