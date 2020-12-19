"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

# Шестнадцатеричные цифры в строковом представлении.
hex_digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')
base = 16

# Функция для проверки алгоритма.
def test_operation(x:str, y:str) -> tuple:
    """ Функция получает два шестнадцатеричных числа в виде строк и возвращает их сумму и произведение. """
    return (hex(int(x, base) + int(y, base)), hex(int(x, base) * int(y, base)))


def hex_sum(x:str, y:str) -> str:
    """ Получает два шестнадцатиричных числа в виде строк и возвращает сумму этих чисел в том же представлении. """

    # Преобразуем строковые параметры в очереди (deque).
    dx, dy = deque(x), deque(y)

    # Если количество цифр в числах не совпадает, то дописываем нули в начало числа с меньшим количеством цифр до тех пор, пока количество цифр в обоих числах не сравняется.
    if len(dx) < len(dy):
        dx.extendleft(['0'] * (len(dy) - len(dx))) 
    elif len(dx) > len(dy):
        dy.extendleft(['0'] * (len(dx) - len(dy)))

    # Реверсируем очереди, благо у них это шустро, не в пример листу.
    # Ибо складывать мы будем, начиная с последних цифр.
    dx.reverse()
    dy.reverse()

    len_dgt = len(dx) # Цикл удобнее строить по индексам, нежели по элементам.
    res_sum = deque() # Переменная для результата.
    qs = 0 # То, что в народе "держат в уме".

    for i in range(len_dgt):

        # Складываем индексы элементов кортежа hex_digits, под которыми лежат суммируемые цифры из dx и dy, а также то, что было в уме.
        sd = qs + hex_digits.index(dx[i]) + hex_digits.index(dy[i])
        
        # Получаем целую часть и остаток от деления полученной суммы цифр на 16.
        qs, rs = divmod(sd, base)
        
        # Добавляем полученную цифру в начало очереди результата. Ранее полученный остаток является индексом, под которым искомая цифра находится в кортеже hex_digits.
        res_sum.appendleft(hex_digits[rs])

    if qs: # Если по окончанию цикла целая часть отлична от 0,
        res_sum.appendleft(hex_digits[qs]) # Добавляем элемент из hex_digits с индексом qs в начало очереди с результатом.

    return ''.join(res_sum)


def hex_mul(x:str, y:str) -> str:
    """ Получает два шестнадцатиричных числа в виде строк и возвращает произведение этих чисел в том же представлении. """

    # Преобразуем строковые параметры в очереди (deque).
    dx, dy = deque(x), deque(y)

    # Реверсируем очереди, благо у них это шустро, не в пример листу.
    # Ибо складывать мы будем, начиная с последних цифр.
    dx.reverse()
    dy.reverse()

    res_mul = deque(['0']) # Переменная для результата.

    for j in range(len(dy)):

        spam = deque() # Переменная для промежуточных результатов, которые суммируются между собой для получения итогового.
        qm = 0 # То, что в народе "держат в уме".

        for i in range(len(dx)):
            md = qm + (hex_digits.index(dx[i]) * hex_digits.index(dy[j]))
            qm, rm = divmod(md, base)
            spam.appendleft(hex_digits[rm])

        if qm:
            spam.appendleft(hex_digits[qm])

        spam.extend(['0'] * j) # сдвигаем промежуточную сумму на величину, равную индексу цифры, на которую умножают первый множитель.

        res_mul = deque(hex_sum(''.join(res_mul), ''.join(spam)))

    return ''.join(res_mul)

if __name__ == '__main__':
    a = input("Введите первое шестнадцатиричное число: ")
    b = input("Введите второе шестнадцатеричное число: ")

    rc = test_operation(a, b)
    rs = hex_sum(a, b)
    rm = hex_mul(a, b)

    print(f"""Сумма введённых чисел = {rs} или {int(rs, base)}.
        Контрольная сумма: {rc[0]} или {int(rc[0], base)}.
        {'Сумма равна контролю. Круто!!!' if int(rs, base) == int(rc[0], base) else 'Сумма и контроль не совпадают. Косяк!'}.
        Произведение введённых чисел = {rm} или {int(rm, base)}.
        Контрольная сумма: {rc[1]} или {int(rc[1], base)}.
        {'Произведение равно контролю. Круто!!!' if int(rm, base) == int(rc[1], base) else 'Произведение и контроль не совпадают. Косяк!'}.""")

