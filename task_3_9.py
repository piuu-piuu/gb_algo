# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

MIN = -1
MAX = 9
COLS = 3
ROWS = 3

matrix = [[randint(MIN, MAX) for _ in range(COLS)] for _ in range(ROWS)]
print(matrix)

mins = [None for _ in range(COLS)]
for c in range(COLS):
    for r in range(ROWS):
        if mins[c] == None or matrix[r][c] < mins[c]:
            mins[c] = matrix[r][c]

print(mins)

max_min = mins[0]
for i in range(len(mins)):
    if mins[i] > max_min:
        max_min = mins[i]

print(max_min)