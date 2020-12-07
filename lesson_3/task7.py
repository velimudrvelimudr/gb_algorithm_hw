""" В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться. """

from random import random

max_item = 10 # Определяет элемент, больше которого не может быть в списке.
a = [int(random() * max_item) for _ in range(10)]

# Ищем минимальный элемент и его индекс в списке.
min_item = a[0]
min_index = 0

for i in range(len(a)):
    if a[i] < min_item:
        min_item = a[i]
        min_index = i

# Ищем второй минимальный элемент.
sec_min_item = max_item

for i in range(len(a)):
    if i != min_index and a[i] < sec_min_item:
        sec_min_item = a[i]

# Выводим результат
print(a)
print(min_item, sec_min_item)
