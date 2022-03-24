# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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
buff = value_list[min_i]
value_list[min_i] = value_list[max_i]
value_list[max_i] = buff
print(value_list)
