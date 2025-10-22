from __future__ import annotations
from typing import Any, Optional
from .wezel import Wezel


class DrzewoBinarne:
    def __init__(self):
        self.korzen: Optional[Wezel] = None

    def wstaw_rekurencyjnie(
            self,
            wartosc: Any,
            wezel: Optional[Wezel] = None
    ) -> None:
        if self.korzen is None:
            self.korzen = Wezel(wartosc)
            return
        if wezel is None:
            wezel = self.korzen
        if wartosc < wezel.wartosc:
            if wezel.poprzedni is None:
                wezel.poprzedni = Wezel(wartosc)
                return
            self.wstaw_rekurencyjnie(wartosc, wezel.poprzedni)
        elif wartosc > wezel.wartosc:
            if wezel.nastepny is None:
                wezel.nastepny = Wezel(wartosc)
                return
            self.wstaw_rekurencyjnie(wartosc, wezel.nastepny)

    def wstaw_iteracyjnie(self, wartosc: Any) -> None:
        if self.korzen is None:
            self.korzen = Wezel(wartosc)
            return
        wezel = self.korzen
        while True:

            if wartosc < wezel.wartosc:
                if wezel.poprzedni is None:
                    wezel.poprzedni = Wezel(wartosc)
                    return
                wezel = wezel.poprzedni
            elif wartosc > wezel.wartosc:
                if wezel.nastepny is None:
                    wezel.nastepny = Wezel(wartosc)
                    return
                wezel = wezel.nastepny
            else:
                return

    def wstaw(self, wartosc: Any, sposob: str = "iteracyjnie") -> None:
        if sposob == "rekurencyjnie":
            self.wstaw_rekurencyjnie(wartosc)
        else:
            self.wstaw_iteracyjnie(wartosc)

    def usun(self, wartosc: Any) -> None:
        self.korzen = self.usun_rekurencyjnie(self.korzen, wartosc)

    def usun_rekurencyjnie(
            self,
            wezel: Optional[Wezel],
            wartosc: Any
    ) -> Optional[Wezel]:
        if wezel is None:
            return None
        if wartosc < wezel.wartosc:
            wezel.poprzedni = self.usun_rekurencyjnie(wezel.poprzedni, wartosc)
        elif wartosc > wezel.wartosc:
            wezel.nastepny = self.usun_rekurencyjnie(wezel.nastepny, wartosc)
        else:
            if wezel.poprzedni is None:
                return wezel.nastepny
            if wezel.nastepny is None:
                return wezel.poprzedni
            nastepnik = self.min_wezel(wezel.nastepny)
            wezel.wartosc = nastepnik.wartosc
            wezel.nastepny = self.usun_rekurencyjnie(wezel.nastepny,
                                                     nastepnik.wartosc)
        return wezel

    @staticmethod
    def min_wezel(wezel: Wezel) -> Wezel:
        while wezel.poprzedni is not None:
            wezel = wezel.poprzedni
        return wezel

    def VLR(self) -> list[Any]:
        wynik: list[Any] = []
        if self.korzen is None:
            return wynik
        stos: list[Wezel] = [self.korzen]
        while stos:
            x = stos.pop()
            wynik.append(x.wartosc)
            if x.nastepny is not None:
                stos.append(x.nastepny)
            if x.poprzedni is not None:
                stos.append(x.poprzedni)
        return wynik

    def LVR(self) -> list[Any]:
        wynik: list[Any] = []
        stos: list[Wezel] = []
        wezel = self.korzen
        while wezel is not None or stos:
            while wezel is not None:
                stos.append(wezel)
                wezel = wezel.poprzedni
            wezel = stos.pop()
            wynik.append(wezel.wartosc)
            wezel = wezel.nastepny
        return wynik

    def LRV(self) -> list[Any]:
        wynik: list[Any] = []
        if self.korzen is None:
            return wynik
        stos1: list[Wezel] = [self.korzen]
        stos2: list[Wezel] = []
        while stos1:
            x = stos1.pop()
            stos2.append(x)
            if x.poprzedni is not None:
                stos1.append(x.poprzedni)
            if x.nastepny is not None:
                stos1.append(x.nastepny)
        while stos2:
            wynik.append(stos2.pop().wartosc)
        return wynik
