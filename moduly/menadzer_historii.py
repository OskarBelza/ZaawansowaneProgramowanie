from __future__ import annotations
from typing import Optional
from struktury import Stos


class MenadzerHistorii:
    def __init__(self) -> None:
        self.historia = Stos()

    def wykonaj_akcje(self, opis: str) -> None:
        self.historia.push(opis)
        print(f'Wykonano akcję: "{opis}"')

    def cofnij(self) -> Optional[str]:
        if self.historia.is_empty():
            print("Brak akcji do cofnięcia.")
            return None
        akcja = self.historia.pop()
        print(f'Cofnięto akcję: "{akcja}"')
        return akcja

    def aktualny_stan(self) -> Optional[str]:
        if self.historia.is_empty():
            print("Brak akcji w historii.")
            return None
        akcja = self.historia.peek()
        print(f'Aktualna akcja: "{akcja}"')
        return akcja
