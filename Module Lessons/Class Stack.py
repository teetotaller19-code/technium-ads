"""
Пошаговый туториал по реализации стека в Python
"""

# Импорт для аннотаций типов
from typing import Any

# Шаг1: Создание класса Stack
class Stack:
    """
    Реализация структуры данных "стек".
    Стек работает по принципу LIFO (последним пришел - первым вышел).
    Поддерживает операции добавления, удаления и просмотра верхнего элемента.
    Предназначен для учебных и алгоритмических задач.
    """

    def __init__(self) -> None:
        self.items: list[Any] = []

    # Шаг 2: Метод is_empty
    def is_empty(self) -> bool:
        return not self.items

    # Шаг 3: Метод push
    def push(self, item: Any) -> None:
        self.items.append(item)

    # Шаг 4: Метод pop
    def pop(self) -> Any:
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('Stack is empty')

    # Шаг 5: Метод peek
    def peek(self) -> Any:
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Stack is empty')

    # Шаг 6: Метод size
    def size(self) -> int:
        return len(self.items)


def main():
    # Шаг 7: Тестирование стека.
    # Создаем экземпляр стека
    my_stack = Stack()

    # Добавляем элементы в стек
    my_stack.push(5)
    my_stack.push(10)
    my_stack.push(15)

    # Просматриваем вершину стека
    print("Вершина стека:", my_stack.peek())

    # Удаляем элемент из стека
    my_stack.pop()

    # Проверяем, пуст ли стек
    print("Стек пуст?", my_stack.is_empty())

    # Выводим размер стека
    print("Размер стека:", my_stack.size())

if __name__ == "__main__":
    main()