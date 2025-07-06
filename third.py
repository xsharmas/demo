#Write a Python function to find the shortest path in a weighted graph using **Dijkstra's algorithm**.  
#Then extend the function to also handle negative weights using **Bellman-Ford algorithm**. 
import heapq
def dijkstra(graph, start):
    """Find the shortest path in a weighted graph using Dijkstra's algorithm."""
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    shortest_path = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, shortest_path
def bellman_ford(graph, start):
    """Find the shortest path in a weighted graph using Bellman-Ford algorithm."""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    shortest_path = {}

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    shortest_path[neighbor] = node

    # Check for negative weight cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")

    return distances, shortest_path
def main():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_node = 'A'

    print("Dijkstra's Algorithm:")
    distances, shortest_path = dijkstra(graph, start_node)
    print(f"Distances: {distances}")
    print(f"Shortest Path: {shortest_path}")

    # Example with negative weights
    graph_with_negative_weights = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': -2, 'D': 5},
        'C': {'A': 4, 'B': -2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    print("\nBellman-Ford Algorithm:")
    try:
        distances_bf, shortest_path_bf = bellman_ford(graph_with_negative_weights, start_node)
        print(f"Distances: {distances_bf}")
        print(f"Shortest Path: {shortest_path_bf}")
    except ValueError as e:
        print(e)
if __name__ == "__main__":
    main()
# This code implements Dijkstra's algorithm for finding the shortest path in a weighted graph
# and extends it to handle negative weights using the Bellman-Ford algorithm.


