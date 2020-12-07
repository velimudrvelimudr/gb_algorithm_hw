""" В массиве случайных целых чисел поменять местами минимальный и максимальный элементы. """

from random import random

a = [int(random() * 10) for _ in range(10)]

# Ищем индексы  минимального и максимального элементов (Если таковых несколько, то берутся с наименьшими индексами).

min_item, max_item = 0, 0

for i in range(len(a)):
    if a[i] < a[min_item]:
        min_item = i
    if a[i] > a[max_item]:
        max_item = i

# Выводим исходный список и индексы минимального и максимального элементов.
print(a)
print(min_item, max_item)

# Меняем элементы местами.
a[min_item], a[max_item] = a[max_item], a[min_item]

# Выводим изменённый список.
print(a)
