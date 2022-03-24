# Определить, какое число в массиве встречается чаще всего.

from random import randint

MIN = 1
MAX = 9
LIST_SIZE = 10

value_list = [randint(MIN, MAX) for _ in range(LIST_SIZE)]

most_freq = None
freq = 0
d = {}
for e in value_list:
    d[e] = d.get(e, 0) + 1
    if d[e] > freq:
        most_freq = e
        freq = d[e]
print(value_list)
print(most_freq)