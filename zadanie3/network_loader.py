import csv
from typing import Dict

GraphType = Dict[str, Dict[str, int]]


def load_network_from_csv(file_path: str) -> GraphType:
    """
    Wczytuje topologię sieci z pliku CSV.
    Format: RouterA,RouterB,PingMs
    Zwraca: Słownik reprezentujący graf nieskierowany (listy sąsiedztwa).
    """
    graph: GraphType = {}

    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)

            for line_num, row in enumerate(reader, 1):
                if not row or len(row) != 3:
                    continue

                try:
                    node_a = row[0].strip()
                    node_b = row[1].strip()
                    cost = int(row[2].strip())
                except ValueError:
                    print(f"⚠️ Ostrzeżenie: Błędna waga w linii {line_num}. Pomijam.")
                    continue

                if node_a not in graph:
                    graph[node_a] = {}
                if node_b not in graph:
                    graph[node_b] = {}

                graph[node_a][node_b] = cost
                graph[node_b][node_a] = cost

    except FileNotFoundError:
        print(f"❌ Błąd: Nie znaleziono pliku '{file_path}'.")
        return {}
    except Exception as e:
        print(f"❌ Nieoczekiwany błąd: {e}")
        return {}

    return graph


if __name__ == "__main__":
    g = load_network_from_csv("siec.csv")
    import json

    print(json.dumps(g, indent=2))