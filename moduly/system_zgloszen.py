from __future__ import annotations
from typing import Optional, Tuple
from struktury import Kolejka


class SystemZgloszen:
    def __init__(self) -> None:
        self.kolejka_zgloszen = Kolejka()

    def dodaj_zgloszenie(self, klient_id: int, kategoria: str) -> None:
        zgloszenie: Tuple[int, str] = (klient_id, kategoria)
        self.kolejka_zgloszen.enqueue(zgloszenie)
        print(f"Dodano zgłoszenie:" f" Klient {klient_id}," f' Kategoria "{kategoria}"')

    def obsluz_nastepne(self) -> Optional[Tuple[int, str]]:
        if self.kolejka_zgloszen.is_empty():
            print("Brak zgłoszeń do obsłużenia.")
            return None
        klient_id, kategoria = self.kolejka_zgloszen.dequeue()
        print(
            f"Obsłużono zgłoszenie:" f" Klient {klient_id}," f' Kategoria "{kategoria}"'
        )
        return klient_id, kategoria

    def liczba_oczekujacych(self) -> int:
        liczba = len(self.kolejka_zgloszen)
        print(f"Liczba oczekujących zgłoszeń: {liczba}")
        return liczba
