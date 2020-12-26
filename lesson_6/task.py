""" Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Выбрал задачу 9 из 3 урока.

Она же - задача 1 из 4 урока.

Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import random
from sys import getsizeof as gso

# Копируем в отдельную переменную список имён тех объектов, которые инициализируются до начала работы программы. 
variables = list(globals().keys()).copy() 

algorithm_number = int(input("Введите номер измеряемого алгоритма - 1, 2 или 3: "))

""" Формируем двумерную матрицу из r строк и c столбцов и заполняем её натуральными числами от 0 до max_num. """
matrix = []
r = 10
c = 10
max_num = 100
for row_cr in range(r):
    matrix.append([])
    for column_cr in range(c):
        matrix[row_cr].append(int(random() * max_num))

size = 0 # Сюда записывается размер потраченной памяти.

# Сразу замеряем суммарный размер элементов матрицы, но без размера самой матрицы.
for rm in range(len(matrix)):
    size += gso(matrix[rm])
    for cm in range(len(matrix[rm])):
        size += gso(matrix[rm][cm])

# print(f"Размер матрицы: {size}.")

if algorithm_number == 1:
    """ возвращает максимальное значение среди минимальных значений в толбцах матрицы. Вариант 1."""
    # Формируем список минимальных значений в столбцах.
    min_items = []
    for column_ch in range(len(matrix[0])):
        min_item = matrix[0][column_ch]
        for row_ch   in range(len(matrix)):
            min_item = matrix[row_ch][column_ch] if matrix[row_ch][column_ch] < min_item else min_item
        min_items.append(min_item)

    # Ищем максимальный элемент в полученном списке.
    max_min_item = min_items[0]
    for item in min_items:
        max_min_item = item if item > max_min_item else max_min_item

    # print(max_min_item)

    # Замеряем суммарный размер элементов списка min_items без учёта размера самого списка.
    size += sum([gso(mitem) for mitem in min_items])
    
    # Обращает на себя внимание то, что переменная внутри генераторного выражения (mitem, в данном случае) не попадает в список глобальных имён.
    # В то же время, переменная item играющая ту же роль в обычном цикле оказывается в глобальном списке. В любом случае, не стал разворачивать выражение в полный цикл.
    # Нужно раскомментировать последний print в программе, чтобы убедиться в этом).

elif algorithm_number == 2:
    """ возвращает максимальное значение среди минимальных значений в толбцах матрицы. вариант 2. """

    min_items = []
    for column_ch in range(len(matrix[0])):
        row = []
        for row_ch in range(len(matrix)):
            row.append(matrix[row_ch][column_ch])
        min_items.append(min(row))

    # print(max(min_items))

    # Замеряем суммарный размер элементов списков min_items и row.
    size += sum([gso(mitem) for mitem in min_items]) + sum([gso(ritem) for ritem in row])

elif algorithm_number == 3:
    """ возвращает максимальное значение среди минимальных значений в толбцах матрицы. Вариант 3. """

    max_min_item = 0
    for column_ch in range(len(matrix[0])):
        min_item = matrix[0][column_ch]
        for row_ch in range(len(matrix)):
            min_item = matrix[row_ch][column_ch] if matrix[row_ch][column_ch] < min_item else min_item
        max_min_item = min_item if min_item > max_min_item else max_min_item

    # print(max_min_item)
else:
    print(f"Вы ввели некорректное число {algorithm_number}. Выходим!")
    exit(0)

size += sum([gso(globals()[k]) for k in globals() if k not in variables])
print(f"Общий размер всех переменных: {size}.")
# print(*[(k, gso(globals()[k])) for k in globals() if k not in variables])

"""
Для каждого из исследуемых алгоритмов формируется одна и таже двумерная матрица случайных целых положительных чисел в интервале 0 - 100. Поскольку размер матрицы константен для всех трёх вариантов кода, то при исследовании алгоритмов он вычитается из суммарного объёма задействованной памяти.

5808 - 4640 = 1168
6204 - 4640 = 1564
5332 - 4640 = 692

Как и следовало ожидать, наилучшие результаты по работе с памятью показал алгоритм 3. В нём совсем не использовались сложные изменяемые типы данных. Он добавляет всего ок. 700 байт к памяти, занимаемой матрицей.
Наихудшие результаты показал 2 алгоритм, где активно использовались списки. Он добавляет ок. 1,5 кб. к объёму матрицы.
Первый алгоритм занял промежуточное место, добавив к матрице чуть более 1 кб.
В процентах это, соответственно, 13%, 25% и 20%.
"""
