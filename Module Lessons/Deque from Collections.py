from collections import deque

# Создание двусторонней очереди
deque_queue = deque()

# Добавление элементов в начало и конец очереди
deque_queue.appendleft(1)   # Добавление в начало
deque_queue.append(2)   # Добавление в конец

# Извлечение элементов с начала и конца очереди
front_element = deque_queue.popleft() # Извлечение с начала
rear_element = deque_queue.pop()    # Извлечение с конца

print("Front Element:", front_element)
print("Rear Element:", rear_element)