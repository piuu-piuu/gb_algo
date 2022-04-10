# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. 
# При этом каждое число представляется как коллекция, элементы которой — цифры числа. 
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
from copy import deepcopy


# ввод
a = deque(input('введите первое число: '))
b = deque(input('введите второе число: '))


# дефолтные тестовые значения, если ввод пустой или неполный
if a == deque([]) or b ==deque([]):
    a = deque(['A', '2'] )
    b = deque(['C', '4', 'F'])    

registers = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

# сумма двух цифр, имитация столбика
def sum_two(x, y, add_on=0, reg = registers):
    notation_size = len(reg)
    index_sum = reg.index(x) + reg.index(y) + add_on
    add_on = index_sum//notation_size
    index_current = index_sum%notation_size
    return reg[index_current], add_on


# проход по первому числу каждой цифрой второго
def h_sum(a,b, reg = registers):
    sum_res = deque([])
    dif = len(a)-len(b)
    if dif >0:
        b.extendleft('0'*(dif))
    else:
        a.extendleft('0'*(-dif))
    a.extendleft('0')
    b.extendleft('0')
    add_on = 0
    for i in range(len(a)-1,-1,-1):
        result = sum_two(a[i], b[i], add_on, reg)
        add_on = result[1]
        sum_res.appendleft(result[0])
    a.popleft()
    b.popleft()
    while sum_res[0] == '0':
        sum_res.popleft()
    return sum_res

def hex_to_dec(n, reg=registers):
    dec = 0
    i = 0
    for value in reversed(n):
        dec = dec + registers.index(value)*len(reg)**i
        i+=1
    return dec

# умножение реализовано через сложение
def mult(a,b):
    mult_res = deepcopy(a)
    for i in range(hex_to_dec(b)-1):
        mult_res = h_sum(mult_res, a)
    return mult_res



print(list(h_sum(a,b)))    
print(list(mult(a,b)))
