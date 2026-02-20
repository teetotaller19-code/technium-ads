"""
Реализация кода обхода графа в ширину (Breadth-First Search).
"""

# Импорт библиотеки deque
from collections import deque

# Определяем функцию обхода графа в ширину
def bfs(graph: dict[int, list[int]], start: int) -> None:
    """
    Выполняет обход графа в ширину.
    :param graph: Граф для обхода.
    :param start: Начальная вершина графа.
    :return: None
    """
    # Множество для отслеживания посещенных вершин
    visited: set[int] = set()
    # Очередь для обхода
    queue: deque[int] = deque()

    # Добавление начальной вершины в очередь и пометка её как посещенной
    queue.append(start)
    visited.add(start)

    # Основной цикл обхода
    while queue:
        # Извлечение вершины из начала очереди
        vertex: int = queue.popleft()
        print(vertex) # Посещаем вершину (выполняем необходимые действия)

        # Добавляем смежные вершины в очередь
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Тестируем функцию обхода в ширину
def main():
    graph = {
        0: [1, 2, 3],
        1: [0, 2],
        2: [0, 1, 4],
        3: [0],
        4: [2]
    }

    bfs(graph, 0)

if __name__ == '__main__':
    main()