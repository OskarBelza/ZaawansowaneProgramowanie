from __future__ import annotations
from typing import Any, Iterator, Optional
from .wezel import Wezel


class ListaJednokierunkowa:
    def __init__(self) -> None:
        self.glowa: Optional[Wezel] = None

    def dodaj_na_poczatku(self, wartosc: Any) -> None:
        self.glowa = Wezel(wartosc, self.glowa)

    def dodaj_na_koncu(self, wartosc: Any) -> None:
        if self.glowa is None:
            self.dodaj_na_poczatku(wartosc)
            return
        aktualny = self.glowa
        while aktualny.nastepny is not None:
            aktualny = aktualny.nastepny
        aktualny.nastepny = Wezel(wartosc)

    def usun_na_poczatku(self) -> None:
        if self.glowa is not None:
            self.glowa = self.glowa.nastepny

    def usun_na_koncu(self) -> None:
        if self.glowa is None:
            return
        if self.glowa.nastepny is None:
            self.glowa = None
            return
        aktualny = self.glowa
        while aktualny.nastepny and aktualny.nastepny.nastepny is not None:
            aktualny = aktualny.nastepny
        aktualny.nastepny = None

    def __iter__(self) -> Iterator[Any]:
        aktualny = self.glowa
        while aktualny is not None:
            yield aktualny.wartosc
            aktualny = aktualny.nastepny

    def wyswietl(self) -> None:
        print(" -> ".join(map(str, self)) + " ->")
