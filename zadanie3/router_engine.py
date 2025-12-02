import heapq
from typing import Dict, List, Tuple, Optional

GraphType = Dict[str, Dict[str, int]]


def find_fastest_route(graph: GraphType, start_node: str, end_node: str) -> Tuple[float, List[str]]:
    """
    Znajduje najszybszą trasę algorytmem Dijkstry.

    Args:
        graph: Słownik reprezentujący graf.
        start_node: Nazwa routera początkowego.
        end_node: Nazwa routera końcowego.

    Returns:
        Krotka (całkowity_koszt, lista_routerów_w_trasie).
        Jeśli trasa nie istnieje, zwraca (float('inf'), []).
    """

    if start_node not in graph or end_node not in graph:
        return float('inf'), []

    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0

    previous_nodes = {node: None for node in graph}

    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end_node:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))


    if distances[end_node] == float('inf'):
        return float('inf'), []

    path = []
    current = end_node
    while current is not None:
        path.append(current)
        current = previous_nodes[current]

    path.reverse()

    return distances[end_node], path


if __name__ == "__main__":
    test_graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    cost, route = find_fastest_route(test_graph, 'A', 'D')
    print(f"Trasa A->D: {route} (Koszt: {cost})")
