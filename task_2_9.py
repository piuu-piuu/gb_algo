# 9. Среди натуральных чисел, которые были введены, 
# найти наибольшее по сумме цифр. Вывести на экран 
# это число и сумму его цифр.

def start():
    _digits = 0
    _gtx = 0
    _x = int(input('Введите число: '))
    return greatest(_digits, _gtx, _x)

def r_count(_x, _digitsum):
    if _x == 0:
        return _digitsum
    _digitsum += _x%10
    _x = _x//10
    return r_count(_x, _digitsum)


def greatest(digits, gtx, x):
    if x == 0:
        print(gtx, digits)
        return gtx, digits
    currentsum = r_count(x, 0)
    if currentsum > digits:
        digits = currentsum
        gtx = x
    x = int(input('Введите число: '))
    greatest(digits, gtx, x)

start()