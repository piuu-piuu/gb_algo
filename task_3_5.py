# В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве. 
# Примечание к задаче: пожалуйста не путайте «минимальный» 
# и «максимальный отрицательный». Это два абсолютно разных значения.

from random import randint

MIN = -9
MAX = 9
LIST_SIZE = 10

value_list = [randint(MIN, MAX) for _ in range(LIST_SIZE)]
print(value_list)

max_neg = None
pos = None
for i, e in enumerate(value_list):
    if e >= 0:
        continue
    if max_neg == None:
        max_neg = e
        pos = i
    else:
        if e > max_neg:
            max_neg = e
            pos = i
print(max_neg, pos)
    