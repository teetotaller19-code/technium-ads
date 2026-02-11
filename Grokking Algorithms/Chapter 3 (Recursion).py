"""
Рекурсия
"""

# Основы рекурсии
# Каждая рекурсивная функция состоит из двух частей:
# базового случая и рекурсивного случая
def countdown(i):
    print(i)
    # Базовый случай
    if i <= 1:
        return
    # Рекурсивный случай
    else:
        countdown(i - 1)

countdown(3)

# Стек вызовов
def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok bye!")

greet("maggie")

# Стек вызовов с рекурсией
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(3))