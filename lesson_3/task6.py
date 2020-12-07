""" В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать. """

from random import random

a = [int(random() * 100) for _ in range(10)]

min_item, max_item = 0, 0

# Если в списке содержатся несколько максимальных или минимальных элементов, то сумма вычисляется между теми из них, у которых наименьший индекс.

for i in range(len(a)):
    if a[i] < a[min_item]:
        min_item = i
    if a[i] > a[max_item]:
        max_item = i

sum_items = 0
step = 0

# Определяем шаг для среза в зависимости от взаимного расположения минимального и максимального элементов.
step = 1 if min_item < max_item else -1

if step != 0:
    for i in a[min_item + step:max_item:step]:
        sum_items += i
else:
    sum_items = 0

# Выводим результат.
print(a)
print(sum_items)
