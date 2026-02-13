"""
Пошаговая реализация очереди в Python
"""

# Импорт для аннотаций типов
from typing import Any

# Шаг1: Создание класса Queue
class Queue:
    """
    Реализация структуры данных "очередь".
    Очередь работает по принципу FIFO (первым пришел - первым вышел).
    Поддерживает операции добавления и извлечения элемента.
    Предназначена для учебных и алгоритмических задач.
    """

    # Шаг 2: Инициализация пустой очереди
    def __init__(self) -> None:
        self.items: list[Any] = []

    # Шаг 3: Метод проверки на пустоту очереди "is_empty"
    def is_empty(self) -> bool:
        return not self.items

    # Шаг 4: Метод постановки элемента в очередь "enqueue"
    def enqueue(self, item: Any) -> None:
        self.items.append(item)

    # Шаг 5: Метод извлечения элемента из очереди "dequeue"
    def dequeue(self) -> Any:
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('Queue is empty')

    # Шаг 6: Метод возврата длины очереди "size"
    def size(self) -> int:
        return len(self.items)


def main():
    # Шаг 7: Тестирование очереди.
    # Создаем экземпляр очереди
    queue = Queue()

    # Добавляем элементы в очередь
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Выводим размер очереди
    print("Размер очереди:", queue.size())

    # Извлекаем элементы из очереди
    while not queue.is_empty():
        item = queue.dequeue()
        print("Извлечен элемент:", item)

if __name__ == "__main__":
    main()