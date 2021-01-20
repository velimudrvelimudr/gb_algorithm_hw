from random import random

def merge_sort(data: list[int]) -> list[int]:
    """ Алгоритм сортировки слиянием из Википедии. """
    count = len(data)
    if count > 2:
        part_1 = merge_sort(data[:count // 2])
        part_2 = merge_sort(data[count // 2:])
        data = part_1 + part_2
        last_index = len(data) - 1

        for i in range(last_index):
            min_value = data[i]
            min_index = i

            for j in range(i + 1, last_index + 1):
                if min_value > data[j]:
                    min_value = data[j]
                    min_index = j

            if min_index != i:
                data[i], data[min_index] = data[min_index], data[i]

    elif len(data) > 1 and data[0] > data[1]:
        data[0], data[1] = data[1], data[0]

    return data

def my_sort(arr: list[float]) -> list[float]: 
    res = []
    h1 = 0
    e1 = (len(arr)) // 2 -1
    h2 = (len(arr)) // 2
    e2 = len(arr)

    for i in range(e2):
        if h1 <= e1:
            if h2 == e2 or arr[h1] <= arr[h2]:
                res.append(arr[h1])
                h1 +=1
            else:
                res.append(arr[h2])
                h2 += 1

    res.extend(arr[h2:])
    return res

# Создаём два отсортированных массива. Второй равен или на 1 элемент больше первого.
arr1 = merge_sort([round(random() * 50, 2) for i in range(5)])
arr2 = merge_sort([round(random() * 50, 2) for i in range(6)])

arr = arr1 + arr2 # Массив, который будем сортировать слиянием.
print(arr)
print(my_sort(arr))

""" На большее меня не хватило... """