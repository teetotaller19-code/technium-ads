"""
Реализация классов для графа, его вершин (узлов) и для BFS.
"""

# Импорт двухсторонней очереди
from collections import deque

# Реализация класса узла
class Node:
    """
    Представляет вершину ориентированного графа с атрибутами в виде
    значения вершины и списками входящих и исходящих рёбер.
    """
    # Инициализация узла
    def __init__(self, value: str):
        self.value: str = value  # Значение узла

        self.outbound: list[Node] = []  # Список исходящих рёбер из узла
        self.inbound: list[Node] = []   # Список входящих рёбер в узел

    # Метод для создания направленного ребра от текущего узла к другому узлу
    def point_to(self, other: Node):
        """
        Добавляет направленное ребро self -> other.
        """
        self.outbound.append(other)
        other.inbound.append(self)

    # Красивый вывод
    def __str__(self):
        return f'Node({self.value})'

    # Красивый вывод для контейнера
    def __repr__(self):
        return self.__str__()

# Реализация класса графа
class Graph:
    """
    Представляет ориентированный граф с возможностью обхода в глубину (DFS) и в ширину (BFS).
    Обход осуществляется по исходящим рёбрам (outbound).
    """
    # Инициализация начального узла
    def __init__(self, root: Node):
        self._root = root

    # Метод для поиска в глубину через стек
    def dfs(self) -> list[str]:
        """
        Выполняет обход графа в глубину (DFS),
        начиная с корневой вершины.

        :return: Список вершин в порядке обхода.
        """
        stack: list[Node] = [self._root]
        visited: set[Node] = set()
        result: list[str] = []
        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                result.append(current_node.value)
                stack.extend(reversed(current_node.outbound))
        return result

    # Метод для поиска в ширину через двухстороннюю очередь
    def bfs(self) -> list[str]:
        """
        Выполняет обход графа в ширину (BFS),
        начиная с корневой вершины.

        :return: Список вершин в порядке обхода.
        """
        visited: set[Node] = set()
        result: list[str] = []
        queue: deque[Node] = deque()

        queue.append(self._root)
        visited.add(self._root)

        while queue:
            vertex: Node = queue.popleft()
            result.append(vertex.value)

            for neighbor in vertex.outbound:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return result

# Тестируем
def main():
    # Тест 1
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    a.point_to(b)
    b.point_to(c)
    c.point_to(d)
    d.point_to(a)
    b.point_to(d)

    graph_1 = Graph(a)
    print(graph_1.dfs())
    print(graph_1.bfs())

    # Тест 2
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    a.point_to(b)
    b.point_to(c)
    c.point_to(d)
    d.point_to(a)
    b.point_to(d)
    b.point_to(f)
    c.point_to(e)

    graph_2 = Graph(a)
    print(graph_2.dfs())
    print(graph_2.bfs())

    # Тест 3
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')
    k = Node('k')
    a.point_to(b)
    b.point_to(c)
    c.point_to(d)
    d.point_to(a)
    b.point_to(d)
    a.point_to(e)
    e.point_to(f)
    e.point_to(g)
    f.point_to(i)
    f.point_to(h)
    g.point_to(k)

    graph_3 = Graph(a)
    print(graph_3.dfs())
    print(graph_3.bfs())

if __name__ == '__main__':
    main()