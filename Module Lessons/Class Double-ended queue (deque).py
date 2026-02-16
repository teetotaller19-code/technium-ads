"""
Пошаговый туториал по реализации двухсторонней очереди в Python
"""

# Импорт для аннотаций типов
from typing import Any

# Шаг 1: Создание класса двухсторонней очереди
class Deque:
    """
    Реализация универсальной структуры данных "двухсторонняя очередь".
    Работает по обоим принципам: как FIFO, так и LIFO.
    Поддерживает операции добавления элемента (в начало или конец),
    извлечение элемента (с начала или конца).
    Предназначена для учебных и алгоритмических задач.
    """

    # Шаг 2: Инициализация пустой очереди
    def __init__(self):
        self.items: list[Any] = []

    # Шаг 3: Метод добавления элемента в начало очереди "add_front"
    def add_front(self, item: Any) -> None:
        self.items.insert(0, item)

    # Шаг 4: Метод добавления элемента в конец очереди "add_rear"
    def add_rear(self, item: Any) -> None:
        self.items.append(item)

    # Шаг 5: Метод извлечения элемента с начала очереди "remove_front"
    def remove_front(self) -> Any:
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Двухсторонняя очередь пуста")

    # Шаг 6: Метод извлечения элемента с конца очереди "remove_rear"
    def remove_rear(self) -> Any:
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Двухсторонняя очередь пуста")

    # Шаг 7: Метод проверки очереди на пустоту "is_empty"
    def is_empty(self) -> bool:
        return not self.items

    # Шаг 8: Метод возврата длины очереди "size"
    def size(self) -> int:
        return len(self.items)

    # Шаг 10: Метод отображения текущего состояния очереди
    def display(self) -> list[Any]:
        return list(self.items)

def main():
    # Шаг 10: Пример использования очереди.
    # Создаем экземпляр очереди
    deque = Deque()

    # Добавляем элементы в очередь и отображаем очередь
    # после каждой операции
    deque.add_front(1)
    print("Очередь после добавления 1 в начало:", deque.display())

    deque.add_rear(2)
    print("Очередь после добавления 2 в конец:", deque.display())

    deque.add_front(3)
    print("Очередь после добавления 3 в начало:", deque.display())

    # Выводим размер очереди
    print("Размер очереди:", deque.size())

    # Визуализируем извлечение элементов из очереди
    front_element = deque.remove_front()
    print("Извлечен элемент с начала:", front_element)
    print("Очередь после извлечения с начала:", deque.display())

    rear_element = deque.remove_rear()
    print("Извлечен элемент с конца:", rear_element)
    print("Очередь после извлечения с конца:", deque.display())

    print("Очередь пуста:", deque.is_empty())

if __name__ == "__main__":
    main()