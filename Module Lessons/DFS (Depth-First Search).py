"""
Реализация рекурсивного алгоритма поиска в глубину (DFS)
"""

# Объявляем граф в виде списка смежности
# Ключи - вершины графа, значения - списки соседей
graph_example: dict[int, list[int]] = {
    0: [1, 2, 3],
    1: [0, 2],
    2: [0, 1, 4],
    3: [0],
    4: [2]
}

def dfs(graph: dict, vertex: int, visited: list) -> None:
    """
    Выполняет поиск в глубину с отображением всех посещенных вершин
    """
    if vertex not in visited:
        print(vertex, end=' ')
        visited.append(vertex)
        for neighbor in graph[vertex]:
            dfs(graph, neighbor, visited)

def main():
    # Пример использования
    dropped_by: list[int] = []
    dfs(graph_example, 0, dropped_by)

if __name__ == '__main__':
    main()