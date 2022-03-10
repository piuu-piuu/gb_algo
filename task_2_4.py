# 4. Найти сумму n элементов следующего ряда чисел: 
# 1, -0.5, 0.25, -0.125,… Количество элементов (n) 
# вводится с клавиатуры.


def start():
    _n = int(input('Введите количество элементов: '))
    _x = 1
    _sum = 1
    _n -= 1
    return r_seq(_x, _n, _sum)

def r_seq(x, n, sum):
    if n == 0:
        print('Сумма ', sum)
        return None
    x = x / -2
    sum += x
    n -= 1
    return r_seq(x, n, sum)

start()