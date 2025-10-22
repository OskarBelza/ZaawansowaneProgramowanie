from struktury import ListaJednokierunkowa, ListaDwukierunkowa
from moduly import MenadzerHistorii, SystemZgloszen


def test_lista_jednokierunkowa():
    print("\n=== TEST: Lista Jednokierunkowa ===")
    lista = ListaJednokierunkowa()
    lista.dodaj_na_poczatku(10)
    lista.dodaj_na_poczatku(5)
    lista.dodaj_na_koncu(15)
    lista.dodaj_na_koncu(20)
    lista.wyswietl()
    lista.usun_na_poczatku()
    lista.wyswietl()
    lista.usun_na_koncu()
    lista.wyswietl()


def test_lista_dwukierunkowa():
    print("\n=== TEST: Lista Dwukierunkowa ===")
    lista = ListaDwukierunkowa()
    lista.dodaj_na_poczatku("A")
    lista.dodaj_na_koncu("B")
    lista.dodaj_na_koncu("C")
    lista.dodaj_na_poczatku("START")
    lista.wyswietl_od_poczatku()
    lista.wyswietl_od_konca()
    lista.usun_na_poczatku()
    lista.wyswietl_od_poczatku()
    lista.usun_na_koncu()
    lista.wyswietl_od_poczatku()


def test_menedzer_i_system():
    print("\n=== TEST: Menedżer Historii (Stos) ===")
    men = MenadzerHistorii()
    men.wykonaj_akcje("Utworzono nowy plik")
    men.wykonaj_akcje("Zapisano tytuł")
    men.aktualny_stan()
    men.cofnij()
    men.wykonaj_akcje("Dodano obrazek")
    men.cofnij()
    men.cofnij()
    men.cofnij()

    print("\n=== TEST: System Zgłoszeń (Kolejka) ===")
    sysz = SystemZgloszen()
    sysz.dodaj_zgloszenie(10, "Sieć")
    sysz.dodaj_zgloszenie(20, "Konto")
    sysz.liczba_oczekujacych()
    sysz.obsluz_nastepne()
    sysz.dodaj_zgloszenie(30, "Płatność")
    sysz.liczba_oczekujacych()
    sysz.obsluz_nastepne()
    sysz.obsluz_nastepne()
    sysz.obsluz_nastepne()


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("START TESTÓW PROJEKTOWYCH")
    print("=" * 60)

    test_lista_jednokierunkowa()
    test_lista_dwukierunkowa()
    test_menedzer_i_system()

    print("\n" + "=" * 60)
    print("KONIEC TESTÓW")
    print("=" * 60)
