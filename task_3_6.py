# В одномерном массиве найти сумму элементов, находящихся между 
# минимальным и максимальным элементами. Сами минимальный и максимальный элементы 
# в сумму не включать.

from random import randint

MIN = 1
MAX = 9
LIST_SIZE = 10

value_list = [randint(MIN, MAX) for _ in range(LIST_SIZE)]

if len(value_list) == 1:
    print("Единственный элемент")
else:
    max_i = 0
    min_i = 0
    max_e = value_list[0]
    min_e = value_list[0]
    for i, e in enumerate(value_list):
        if e > max_e:
            max_e = e
            max_i = i
        elif e < min_e:
            min_e = e
            min_i = i
print(value_list)
if max_i < min_i:
    _ = min_i
    min_i = max_i
    max_i = _
e_sum = 0
for i in range(min_i+1, max_i):
    e_sum += value_list[i]
print(e_sum)