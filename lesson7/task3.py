""" 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы. """

from random import randint

q = 5
arr = [randint(0, 100) for _ in range(2*q + 1)]

print(arr)

def get_mediana(arr: list[int]) -> int:
    """ Ищет медиану в списке целых чисел. """
    s = 0
    e = len(arr) 

    while e - s != 1:
        for i in range(s, e - 1, 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        e -= 1
        for i in range(e - 1, s + 1, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        s += 1
    # print(arr)
    return arr[s]

print(f"Медиана = {get_mediana(arr)}")

""" Вроде шейкерная сортировка тут должна быть допустима... А она как раз в тему."""