"""
Алгоритм бинарного поиска
"""

def binary_search(numbers: list[int], item: int) -> int | None:
    """
    Функция принимает первым аргументом отсортированный список целых чисел,
    вторым аргументом целое число для поиска и осуществляет
    бинарный поиск числа в списке

    :param list_arg: список целых чисел
    :param item: целое число, которое будем искать
    :return: индекс найденного числа в списке или None при его отсутствии
    """
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = numbers[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_list, 6))
print(binary_search(my_list, -1))