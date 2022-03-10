# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def start():
    _x = int(input('Введите число: '))
    if _x == 0:
        print('нечетных: ', 0)
        print('четных: ', 1)
        return None
    odd = 0
    even = 0
    r_count(_x, odd, even)

def r_count(x, o, e):
    if x == 0:
        print('нечетных: ', o)
        print('четных: ', e)
        return None
    if x%10%2 == 0:
        e += 1
    else:
        o += 1
    x = x//10
    r_count(x, o, e)

start()