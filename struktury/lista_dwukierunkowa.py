from __future__ import annotations
from typing import Any, Optional
from .wezel import Wezel


class ListaDwukierunkowa:
    def __init__(self) -> None:
        self.glowa: Optional[Wezel] = None
        self.ogon: Optional[Wezel] = None

    def dodaj_na_poczatku(self, wartosc: Any) -> None:
        nowy = Wezel(wartosc)
        if self.glowa is None:
            self.glowa = self.ogon = nowy
        else:
            nowy.nastepny = self.glowa
            self.glowa.poprzedni = nowy
            self.glowa = nowy

    def dodaj_na_koncu(self, wartosc: Any) -> None:
        if self.ogon is None:
            self.dodaj_na_poczatku(wartosc)
            return
        nowy = Wezel(wartosc, None, self.ogon)
        self.ogon.nastepny = nowy
        self.ogon = nowy

    def usun_na_poczatku(self) -> None:
        if self.glowa is None:
            return
        if self.glowa.nastepny is None:
            self.glowa = self.ogon = None
        else:
            self.glowa = self.glowa.nastepny
            self.glowa.poprzedni = None

    def usun_na_koncu(self) -> None:
        if self.ogon is None:
            return
        if self.ogon.poprzedni is None:
            self.glowa = self.ogon = None
        else:
            self.ogon = self.ogon.poprzedni
            self.ogon.nastepny = None

    def wyswietl_od_poczatku(self) -> None:
        cur = self.glowa
        out = []
        while cur is not None:
            out.append(str(cur.wartosc))
            cur = cur.nastepny
        print(" <-> ".join(out) + " <->")

    def wyswietl_od_konca(self) -> None:
        cur = self.ogon
        out = []
        while cur is not None:
            out.append(str(cur.wartosc))
            cur = cur.poprzedni
        print(" <-> ".join(out) + " <->")
