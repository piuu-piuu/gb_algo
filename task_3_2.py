# Во втором массиве сохранить индексы четных элементов первого массива. 
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

from random import randint

MIN = 1
MAX = 100

value_list = [randint(MIN, MAX) for _ in range(MAX)]
index_list = []

for index, value in enumerate(value_list):
    if value%2 == 0:
        index_list.append(index)

print(value_list)
print(index_list)