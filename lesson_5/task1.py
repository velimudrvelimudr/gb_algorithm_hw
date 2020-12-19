""" Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего. """

from collections import namedtuple

def calc_sum(l: list) -> int:
    """ Подсчитывает сумму элементов списка. """
    return sum(l)

firma = namedtuple('firma', 'name, profit_i, profit_ii, profit_iii, profit_iv, calc_sum',
    defaults=['noname', 0, 0 ,0, 0, None])

list_firms = [] # Список фирм.

while True:
    n = input("Введите название фирмы или q для завершения: ")
    if n in ('q', 'Q'):
        break
    pr1 = int(input("Введите прибыль фирмы за I квартал: "))
    pr2 = int(input("Введите прибыль фирмы за II квартал: "))
    pr3 = int(input("Введите прибыль фирмы за III квартал: "))
    pr4 = int(input("Введите прибыль фирмы за IV квартал: "))
    list_firms.append(firma(n, pr1, pr2, pr3, pr4, calc_sum))

# firm_profit = {f.name: f.calc_sum([f.profit_i, f.profit_ii, f.profit_iii, f.profit_iv]) for f in list_firms}

avg_profit = round((sum([f.calc_sum([f.profit_i, f.profit_ii, f.profit_iii, f.profit_iv]) for f in list_firms]) / len(list_firms)), 2)

weak = [] # Слабые компании.
strong = [] # Сильные компании

for f in list_firms:
    year_profit = f.calc_sum([f.profit_i, f.profit_ii, f.profit_iii, f.profit_iv])
    if year_profit > avg_profit:
        strong.append(f)
    else:
        weak.append(f)

# вывод результата
print(f"Средняя годовая прибыль компаний составляет {avg_profit} рублей.")
print(f"Слабые компании.\nИх прибыль ниже или равна среднему значению {avg_profit} рублей.")
print(*[f"{f.name}: {f.calc_sum((f.profit_i, f.profit_ii, f.profit_iii, f.profit_iv))}" for f in weak], sep='\n')

print(f"Сильные компании.\nИх прибыль выше среднего значения {avg_profit} рублей.")
print(*[f"{f.name}: {f.calc_sum((f.profit_i, f.profit_ii, f.profit_iii, f.profit_iv))}" for f in strong], sep='\n')
