"""
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.

Выбрал задачу 9 из 3 урока.

Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

from random import random
from timeit import timeit
from csv import writer

""" Изначальный код не очень подходит для анализа. Поэтому, прежде всего, запаковываем формирование матрицы и нахождение нужного значения в две функции. """
def create_matrix(r: int, c: int, max_num: int=100) -> list:
    """ Формируем двумерную матрицу из r строк и c столбцов и заполняем её натуральными числами от 0 до max_num. """
    matrix = []
    for row in range(r):
        matrix.append([])
        for column in range(c):
            matrix[row].append(int(random() * max_num))
    return matrix


def check_max_min1(m: list) -> int:
    """ возвращает максимальное значение среди минимальных значений в толбцах матрицы. """
    # Формируем список минимальных значений в столбцах.
    min_items = []
    for column in range(len(m[0])):
        min_item = m[0][column]
        for row in range(len(m)):
            min_item = m[row][column] if m[row][column] < min_item else min_item
        min_items.append(min_item)

    # Ищем максимальный элемент в полученном списке.
    max_min_item = min_items[0]
    for i in min_items:
        max_min_item = i if i > max_min_item else max_min_item

    return max_min_item


def check_max_min2(m: list) -> int:
    """ возвращает максимальное значение среди минимальных значений в толбцах матрицы. """

    min_items = []
    for column_number in range(len(m[0])):
        row = []
        for row_number in range(len(m)):
            row.append(m[row_number][column_number])
        min_items.append(min(row))
    return max(min_items)


def check_max_min3(m: list) -> int:
    """ возвращает максимальное значение среди минимальных значений в толбцах матрицы. """

    max_min_item = 0
    for column in range(len(m[0])):
        min_item = m[0][column]
        for row in range(len(m)):
            min_item = m[row][column] if m[row][column] < min_item else min_item
        max_min_item = min_item if min_item > max_min_item else max_min_item
    return max_min_item


def main(rc: int=10, cc: int=10) -> tuple:
    """ Создаём матрицу с размерами rcXcc, и замеряем её обработку тремя разными алгоритмами. """

    mx = create_matrix(rc, cc)
    t1 = timeit('check_max_min1(mx)', globals=globals()|locals())
    t2 = timeit('check_max_min2(mx)', globals=globals()|locals())
    t3 = timeit('check_max_min3(mx)', globals=globals()|locals())

    """ Поскольку вывод timeit производится внутри функции, globals=globals() оказалось недостаточным, ибо timeit не видит mx, объявленную внутри main(). Не знаю, как правильно, но я просто добавил словарь locals() к globals() с помощью инструмента объединения словарей "|", который появился то ли в Python 3.8, то ли в 3.9. """
    return (t1, t2, t3)


# Производим замер, сохраняем результат в csv-файл и печатаем в консоли.
if __name__ == '__main__':
    with open('meas.csv', 'w', encoding='utf-8', newline='') as meas_file:
        csvw = writer(meas_file, dialect='excel-tab')
        for x in range(2, 11):
            meas = main(x, x)
            csvw.writerow([x, meas[0], meas[1], meas[2]])
            print(x, round(meas[0], 3), round(meas[1], 3), round(meas[2], 3), sep='\t')

"""
Результат одного из замеров, взятый из csv-файла.

	алг1	алг2	алг3
2	1,242	1,620	1,132
3	1,934	2,507	1,793
4	2,889	3,532	2,395
5	3,813	4,818	3,301
6	5,121	6,349	4,264
7	6,480	7,817	5,484
8	7,782	9,667	6,543
9	9,246	11,883	7,846
10	10,652	13,977	9,263

В самом левом столбце - размерность матрицы.

Несмотря на то, что во всех алгоритмах присутствуют вложенные циклы, а в первом цикла даже два (второй без вложений), рост времени в зависимости от размерности матрицы является линейным. Ну или близко к тому. И это не смотря на то, что количество элементов, которые обрабатываются, растёт параболически. По форме все три графика явно одинаковы, или различаются очень незначительно.

Если сравнивать абсолютные значения времени для каждой размерности, то дольше всего матрицу обрабатывает 2-й алгоритм, в котором активно используются функции append(), min(), max().
Следующим по эффективности идёт 1-й алгоритм. В нём присутствуют два цикла.
Самым быстрым оказался 3-й алгоритм, за счёт того, что в нём все операции производятся в одном цикле, имеющем вложенный цикл. Сами же операции сведены исключительно к сравнению и присвоению.

Особенно примечательно, что самый быстрый и самый медленный алгоритм фактически одинаковы, различны лишь использованные средства языка.
"""