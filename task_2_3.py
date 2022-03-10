# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр 
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.

def start():
    _x = int(input('Введите число: '))
    if _x == 0:
        print(0)
        return None
    r_digits(_x)

def r_digits(x):
    if x == 0:
        print('')
        return None
    print(x%10, end='')
    x = x//10
    r_digits(x)

start()