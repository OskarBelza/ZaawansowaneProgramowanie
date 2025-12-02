from typing import Optional


class BookNode:
    """
    Węzeł drzewa BST reprezentujący unikalną książkę.
    """

    def __init__(self, isbn: str, title: str):
        self.isbn: str = isbn
        self.title: str = title
        self.count: int = 1  # Licznik duplikatów
        self.left: Optional['BookNode'] = None
        self.right: Optional['BookNode'] = None

    def __repr__(self):
        return f"Node({self.isbn}, {self.count})"


class LibraryBST:
    """
    Drzewo Binarnych Poszukiwań (BST) zarządzające inwentarzem.
    Kluczem sortowania jest ISBN.
    """

    def __init__(self):
        self.root: Optional[BookNode] = None

    def insert(self, isbn: str, title: str) -> None:
        if self.root is None:
            self.root = BookNode(isbn, title)
        else:
            self._insert_recursive(self.root, isbn, title)

    def _insert_recursive(self, node: BookNode, isbn: str, title: str) -> None:
        if isbn == node.isbn:
            node.count += 1
            return

        elif isbn < node.isbn:
            if node.left is None:
                node.left = BookNode(isbn, title)
            else:
                self._insert_recursive(node.left, isbn, title)

        else:
            if node.right is None:
                node.right = BookNode(isbn, title)
            else:
                self._insert_recursive(node.right, isbn, title)

    def generate_report(self) -> None:
        """
        Wypisuje raport posortowany rosnąco po ISBN.
        """
        print("\n--- RAPORT STANÓW MAGAZYNOWYCH (ISBN ASC) ---")
        if self.root is None:
            print("Magazyn jest pusty.")
        else:
            self._in_order(self.root)
        print("---------------------------------------------")

    def _in_order(self, node: Optional[BookNode]) -> None:
        """
        Przechodzi drzewo w kolejności: Lewy -> Rodzic -> Prawy.
        Dzięki temu wartości wypisywane są od najmniejszej do największej.
        """
        if node is None:
            return

        self._in_order(node.left)

        print(f"[{node.isbn}] {node.title} - Ilość: {node.count}")

        self._in_order(node.right)


if __name__ == "__main__":
    lib = LibraryBST()

    data = [
        ("978-83-01", "Pan Tadeusz"),
        ("978-00-01", "Czysty Kod"),
        ("978-83-01", "Pan Tadeusz"),
        ("978-99-99", "Harry Potter"),
        ("978-83-01", "Pan Tadeusz"),
        ("978-50-50", "Wiedźmin")
    ]

    print("Dodawanie książek...")
    for isbn, title in data:
        lib.insert(isbn, title)

    lib.generate_report()