from struktury import ListaJednokierunkowa, ListaDwukierunkowa, DrzewoBinarne
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


def test_drzewo_binarne():
    print("\n=== TEST: Drzewo BST ===")
    drzewo = DrzewoBinarne()

    print("\n--- Wstawianie iteracyjne ---")
    for x in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        drzewo.wstaw(x, "iteracyjnie")
        print("LVR (inorder):", drzewo.LVR())

    print("\n--- Wstawianie rekurencyjne ---")
    for x in [2, 5, 9, 15]:
        drzewo.wstaw(x, "rekurencyjnie")
        print("LVR (inorder):", drzewo.LVR())

    print("\n--- Przejścia drzewa ---")
    print("VLR (preorder):", drzewo.VLR())
    print("LVR (inorder):", drzewo.LVR())
    print("LRV (postorder):", drzewo.LRV())

    print("\n--- Usuwanie węzłów ---")
    for x in [1, 6, 8, 14]:
        print(f"Usuwam: {x}")
        drzewo.usun(x)
        print("Aktualne LVR:", drzewo.LVR())


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("START TESTÓW PROJEKTOWYCH")
    print("=" * 60)

    test_lista_jednokierunkowa()
    test_lista_dwukierunkowa()
    test_menedzer_i_system()
    test_drzewo_binarne()

    print("\n" + "=" * 60)
    print("KONIEC TESTÓW")
    print("=" * 60)
