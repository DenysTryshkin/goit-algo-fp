import networkx as nx
import heapq

# Ініціалізація графа
G = nx.Graph()
cities = ["Париж", "Берлін", "Мадрид", "Рим", "Амстердам", "Відень"]
G.add_nodes_from(cities)

# Додавання ребер з вагами
edges_with_weights = [
    ("Париж", "Берлін", 5),
    ("Париж", "Амстердам", 3),
    ("Берлін", "Відень", 2),
    ("Мадрид", "Рим", 4),
    ("Рим", "Берлін", 1),
    ("Відень", "Мадрид", 6),
    ("Рим", "Амстердам", 7),
]

G.add_weighted_edges_from(edges_with_weights)

# Реалізація алгоритму Дейкстри з використанням бінарної купи
def dijkstra_with_heap(graph, start):
    distances = {node: float("inf") for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    shortest_paths = {node: [] for node in graph.nodes}
    shortest_paths[start] = [start]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Пропускаємо, якщо поточна відстань більше збереженої
        if current_distance > distances[current_node]:
            continue

        # Оновлюємо відстані до сусідів
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]["weight"]
            distance = current_distance + weight

            # Якщо знайдено коротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, shortest_paths

# Обчислюємо найкоротші шляхи для всіх пар вершин
def dijkstra_all_pairs(graph):
    all_shortest_paths = {}
    for city in graph.nodes:
        distances, paths = dijkstra_with_heap(graph, city)
        all_shortest_paths[city] = paths
    return all_shortest_paths

# Виклик функції для знаходження найкоротших шляхів між усіма вершинами
all_shortest_paths = dijkstra_all_pairs(G)

# Виведення результатів
for start_city, paths in all_shortest_paths.items():
    print("********")
    print(f"Найкоротші шляхи від {start_city}:")
    for end_city, path in paths.items():
        distance = nx.path_weight(G, path, weight="weight")
        print(f"До {end_city}: шлях {path}, відстань {distance}")
