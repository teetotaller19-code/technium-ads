"""
Реализация классов для графа, его вершин (узлов) и для DFS.
"""

# Реализация класса узла
class Node:
    """
    Представляет вершину ориентированного графа.
    """
    # Инициализация узла
    def __init__(self, value: str):
        # Атрибут, хранящий значение узла (название вершины)
        self.value = value

        # Список исходящих рёбер из данного узла
        self.outbound: list[Node] = []
        # Список входящих рёбер в данный узел
        self.inbound: list[Node] = []

    # Метод создания направленного ребра от текущего узла к другому узлу
    def point_to(self, other: Node):
        """
        Создает направленное ребро от текущего узла к другому узлу.
        """
        # Добавление другого узла в список исходящих рёбер текущего узла
        self.outbound.append(other)
        # Добавление текущего узла в список входящих рёбер другого узла
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'

    def __repr__(self):
        return self.__str__()

# Реализация класса графа
class Graph:
    """
    Представляет ориентированный граф с возможностью обхода в глубину.
    """
    # Инициализация начального узла
    def __init__(self, root: Node):
        self._root = root

    # Метод для поиска в глубину через список и стек
    def dfs(self) -> list[Node]:
        """
        Выполняет обход графа в глубину (DFS),
        начиная с корневой вершины.

        :return: Список вершин в порядке обхода.
        """
        stack = [self._root]
        visited = []
        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                visited.append(current_node)
                stack.extend(reversed(current_node.outbound))
        return visited

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

if __name__ == '__main__':
    main()