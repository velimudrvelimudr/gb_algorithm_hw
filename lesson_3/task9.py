""" Найти максимальный элемент среди минимальных элементов столбцов матрицы. """

from random import random

# Формируем матрицу.
a = []
for row in range(5):
    a.append([])
    for column in range(4):
        a[row].append(int(random() * 100))

# Вывод матрицы.
# Ну коли уж написал, пусть остаётся в таком виде.
print('\n'.join(['\t'.join(map(str, row)) for row in a]))

# Формируем список минимальных значений в столбцах.
min_items = []
for column in range(4):
    min_item = a[0][column]
    for row in range(5):
        min_item = a[row][column] if a[row][column] < min_item else min_item
    min_items.append(min_item)

print('\t'.join(map(str, min_items)))

# Ищем максимальный элемент в полученном списке.
max_min_item = min_items[0]
for i in min_items:
    max_min_item = i if i > max_min_item else max_min_item

print(str(max_min_item))
