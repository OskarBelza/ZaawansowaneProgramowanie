import sys
from network_loader import load_network_from_csv
from router_engine import find_fastest_route


def main():
    print("=== SYMULATOR TRAS ROUTINGU (Dijkstra) ===")

    filename = "siec.csv"
    print(f"--> Wczytywanie topologii z pliku '{filename}'...")

    network_graph = load_network_from_csv(filename)

    if not network_graph:
        print("Błąd: Nie udało się wczytać sieci. Sprawdź plik CSV.")
        sys.exit(1)

    print(f"--> Załadowano {len(network_graph)} routerów.")

    while True:
        print("\n-------------------------------------------")
        print("Wpisz 'exit' aby zakończyć.")

        start_node = input("Podaj router startowy (np. R1): ").strip()
        if start_node.lower() == 'exit': break

        end_node = input("Podaj router końcowy  (np. R6): ").strip()
        if end_node.lower() == 'exit': break

        print(f"\nObliczam trasę z {start_node} do {end_node}...")

        cost, path = find_fastest_route(network_graph, start_node, end_node)

        if cost == float('inf'):
            print(f"❌ Brak połączenia między {start_node} a {end_node}.")
        else:
            print("✅ ZNALEZIONO NAJSZYBSZĄ TRASĘ!")
            print(f"   Całkowite opóźnienie: {cost} ms")
            path_str = " -> ".join(path)
            print(f"   Ścieżka: {path_str}")


if __name__ == "__main__":
    main()