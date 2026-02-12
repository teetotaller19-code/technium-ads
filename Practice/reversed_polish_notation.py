"""
Необходимо написать программу, реализовывающую обратную польскую запись.
Обратная польская запись (Reverse Polish Notation, RPN - она же постфиксная
нотация, или обратная польская нотация (ОПН)) - это форма записи математических
выражений, в которой операторы располагаются после своих операндов.
Это также называется постфиксной записью. В обратной польской записи порядок
выполнения операций однозначно определяется, и не требуется использование скобок
для указания операций.
Пример обратной польской записи:
Обычное инфиксное выражение: 3 + 4 * 2
Обратная польская запись: 3 4 2 * +
В обратной польской записи каждый операнд считывается, а затем оператор выполняется
над двумя последними операндами. В данном случае, сначала выполняется умножение 4 * 2,
а затем результат (8) складывается с 3, чтобы получить окончательный результат (11)
"""

# Импорт необходимой библиотеки
import operator

# Создаем стек
class Stack:
    """
    Реализация структуры данных "стек".
    Стек работает по принципу LIFO (последним пришел - первым вышел).
    Поддерживает операции добавления, удаления и просмотра верхнего элемента.
    Предназначен для учебных и алгоритмических задач.
    """

    def __init__(self) -> None:
        self.items: list[float] = []

    def is_empty(self) -> bool:
        return not self.items

    def push(self, item: float) -> None:
        self.items.append(item)

    def pop(self) -> float:
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError('Stack is empty')

    def peek(self) -> float:
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError('Stack is empty')

    def size(self) -> int:
        return len(self.items)

# Создаем функцию для обработки ОПН
def reversed_polish_notation(rpn_string: str) -> int | float | str:
    """
    Вычисляет значение математического выражения, подаваемого в виде строки в формате
    обратной польской записи.

    :param rpn_string: Строка в формате обратной польской записи
    :return: Результат вычисления математического выражения или 'Invalid RPN sequence'.
    """
    rpn_stack = Stack()
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '**': operator.pow}
    tokens = rpn_string.split()
    for token in tokens:
        try:
            number = float(token)
            rpn_stack.push(number)
            continue
        except ValueError:
            if token not in operators:
                return 'Invalid RPN sequence'
            if rpn_stack.size() < 2:
                return 'Invalid RPN sequence'
            number2 = rpn_stack.pop()
            number1 = rpn_stack.pop()
            try:
                math_action = operators[token]
                result = math_action(number1, number2)
                rpn_stack.push(result)
            except ZeroDivisionError:
                return 'Invalid RPN sequence'
    if rpn_stack.size() == 1:
        result = rpn_stack.pop()
        return int(result) if result.is_integer() else result
    else:
        return 'Invalid RPN sequence'

# Создаем основную функцию программы
def main() -> None:
    print(reversed_polish_notation('3 4 +'))
    print(reversed_polish_notation('5 1 2 + 4 * + 3 -'))
    print(reversed_polish_notation('2 5 **'))
    print(reversed_polish_notation('3 +'))
    print(reversed_polish_notation('2 3 4 +'))
    print(reversed_polish_notation('+'))
    print(reversed_polish_notation(''))
    print(reversed_polish_notation('5 0 /'))

if __name__ == '__main__':
    main()