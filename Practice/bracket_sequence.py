"""
Необходимо написать программу, проверяющую, является ли данная строка
правильной скобочной последовательностью.
Правильной скобочной последовательностью считается последовательность,
в которой каждая открывающая скобка (например, '(','{','[')
имеет соответствующую закрывающую скобку (')','}',']').
При этом скобки должны быть правильно вложены друг в друга,
и порядок их следования должен быть корректным.
"""

# Объявляем константы
BRACKETS_DICT: dict[str, str] = {')': '(', '}': '{', ']': '['}
OPEN_BRACKETS: set[str] = set(BRACKETS_DICT.values())

# Импорты для аннотаций типов
from typing import Any

# Создаем стек
class Stack:
    """
    Реализация структуры данных "стек".
    Стек работает по принципу LIFO (последним пришел - первым вышел).
    Поддерживает операции добавления, удаления и просмотра верхнего элемента.
    Предназначен для учебных и алгоритмических задач.
    """

    def __init__(self) -> None:
        self.items: list[Any] = []

    def is_empty(self) -> bool:
        return not self.items

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('Stack is empty')

    def peek(self) -> Any:
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Stack is empty')

    def size(self) -> int:
        return len(self.items)

# Создаем функцию проверки скобочной последовательности
def bracket_sequence_checker(bracket_string: str) -> str:
    """
    Проверяет, является ли строка правильной скобочной последовательностью.

    :param bracket_string: Строка, содержащая только символы скобок: (){}[].
    :return: 'Valid bracket sequence', если последовательность корректна, иначе 'Invalid bracket sequence'.
    """
    bracket_stack = Stack()
    for char in bracket_string:
        if char in BRACKETS_DICT:
            if bracket_stack.is_empty() or BRACKETS_DICT[char] != bracket_stack.peek():
                return 'Invalid bracket sequence'
            else:
                bracket_stack.pop()
        elif char in OPEN_BRACKETS:
            bracket_stack.push(char)
        else:
            return 'Invalid bracket sequence'
    return 'Valid bracket sequence' if bracket_stack.is_empty() else 'Invalid bracket sequence'

# Основная функция программы
def main() -> None:
    print(bracket_sequence_checker(''))
    print(bracket_sequence_checker('('))
    print(bracket_sequence_checker('()[]{}'))
    print(bracket_sequence_checker('([{}])'))
    print(bracket_sequence_checker('([)]'))
    print(bracket_sequence_checker('{(})'))
if __name__ == '__main__':
    main()