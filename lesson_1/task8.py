"""
Задание:
Определить, является ли год, который ввел пользователь, високосным или не високосным.

Календарь был введён в 1582 г. Поэтому указание года, предшествующего 1583, не имеет смысла.

год, номер которого кратен 400, — високосный;
другие года, номера которых кратны 100, — невисокосные;
другие года, номер которых кратен 4, — високосные;
остальные года — невисокосные.

Алгоритм.
Запрашиваем у пользователя номер года, начиная с 1583 (параллелограмм)
Если год кратен 400 (ромб),
то выводим, что год високосный (параллелограмм)
иначе если год кратен 100 (ромб)
то выводим, что год не високосный (параллелограмм)
иначе если год кратен 4 (ромб)
то выводим, что год високосный (параллелограмм)
иначе выводим, что год невисокосный (параллелограмм)
"""

year = int(input("Введите любой год, начиная с 1583: "))

if year % 400 == 0:
    print(f"{year} - високосный год")
elif year % 100 == 0:
    print(f"{year} - не високосный год")
elif year % 4 == 0:
    print(f"{year} - високосный год")
else:
    print(f"{year} - не високосный год")
