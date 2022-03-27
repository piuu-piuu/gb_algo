# ПЗ 3.4 Определить, какое число в массиве встречается чаще всего.

from random import randint
import timeit
import cProfile

def arr(size):
    min = 1
    max = 9
    return [randint(min, max) for _ in range(size)]


# co словарем
def dict_fun(value_list):
    most_freq = None
    freq = 0
    d = {}
    for e in value_list:
        d[e] = d.get(e, 0) + 1
        if d[e] > freq:
            most_freq = e
            freq = d[e]
    return most_freq

# со списком
def list_fun(value_list):
    max_freq = 0
    most_freq = -1
    n = len(value_list)
    for i in range(n):
        curr_freq = 1
        for j in range(i+1, n):
            if value_list[j] == value_list[i]:
                curr_freq = curr_freq + 1
        if max_freq < curr_freq:
            max_freq = curr_freq
            most_freq = value_list[i]  
    return most_freq


#со словарем рекурсивно
def rec_fun_init(value_list):
    # header
    most_freq = None
    freq = 0
    d = {}
    i = 0
    size = len(value_list)
    return recur_fun(most_freq, freq, d, i, size, value_list)

def recur_fun(most_freq, freq, d, i, size, value_list):
    if not i < size:
        return most_freq
    e = value_list[i]
    i +=1
    d[e] = d.get(e, 0) + 1
    if d[e] > freq:
        most_freq = e
        freq = d[e]
    return recur_fun(most_freq, freq, d, i, size, value_list)

print(dict_fun(arr(5)))
print(list_fun(arr(5)))
print(rec_fun_init(arr(500)))


print(timeit.timeit('dict_fun(arr(5))', number=100, globals=globals())) # 0.0011411000000407512 
print(timeit.timeit('dict_fun(arr(50))', number=100, globals=globals())) # 0.009056899999905
print(timeit.timeit('dict_fun(arr(100))', number=100, globals=globals())) # 0.017834599999787315
print(timeit.timeit('dict_fun(arr(150))', number=100, globals=globals())) # 0.026675000000068394
print(timeit.timeit('dict_fun(arr(200))', number=100, globals=globals())) # 0.031461399999898276
print(timeit.timeit('dict_fun(arr(250))', number=100, globals=globals())) # 0.0359665999999379
print(timeit.timeit('dict_fun(arr(300))', number=100, globals=globals())) # 0.043397599999934755

cProfile.run('dict_fun(arr(300))')

#          2903 function calls in 0.001 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       300    0.000    0.000    0.000    0.000 random.py:239(_randbelow_with_getrandbits)
#       300    0.000    0.000    0.001    0.000 random.py:292(randrange)
#       300    0.000    0.000    0.001    0.000 random.py:366(randint)
#         1    0.000    0.000    0.001    0.001 task_4_1.py:11(arr)
#         1    0.000    0.000    0.001    0.001 task_4_1.py:14(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_4_1.py:18(dict_fun)
#       900    0.000    0.000    0.000    0.000 {built-in method _operator.index}
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       300    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       300    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
#       497    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


print(timeit.timeit('list_fun(arr(5))', number=100, globals=globals()))  # 0.0013209999997343402
print(timeit.timeit('list_fun(arr(50))', number=100, globals=globals())) # 0.019716699999662524
print(timeit.timeit('list_fun(arr(100))', number=100, globals=globals())) # 0.05476090000001932
print(timeit.timeit('list_fun(arr(150))', number=100, globals=globals())) # 0.06783249999989494
print(timeit.timeit('list_fun(arr(200))', number=100, globals=globals())) # 0.109050500000194
print(timeit.timeit('list_fun(arr(250))', number=100, globals=globals())) # 0.1538630000000012
print(timeit.timeit('list_fun(arr(300))', number=100, globals=globals())) # 0.21788399999968533

cProfile.run('list_fun(arr(300))')

#          2619 function calls in 0.003 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#       300    0.000    0.000    0.000    0.000 random.py:239(_randbelow_with_getrandbits)
#       300    0.000    0.000    0.001    0.000 random.py:292(randrange)
#       300    0.000    0.000    0.001    0.000 random.py:366(randint)
#         1    0.000    0.000    0.001    0.001 task_4_1.py:11(arr)
#         1    0.000    0.000    0.001    0.001 task_4_1.py:14(<listcomp>)
#         1    0.002    0.002    0.002    0.002 task_4_1.py:30(list_fun)
#       900    0.000    0.000    0.000    0.000 {built-in method _operator.index}
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       300    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       512    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}



print(timeit.timeit('rec_fun_init(arr(5))', number=100, globals=globals()))  # 0.0004822999999305466
print(timeit.timeit('rec_fun_init(arr(50))', number=100, globals=globals())) # 0.004017499999918073
print(timeit.timeit('rec_fun_init(arr(100))', number=100, globals=globals())) # 0.008680699999786157
print(timeit.timeit('rec_fun_init(arr(150))', number=100, globals=globals())) # 0.012716199999886157
print(timeit.timeit('rec_fun_init(arr(200))', number=100, globals=globals())) # 0.016602400000010675
print(timeit.timeit('rec_fun_init(arr(250))', number=100, globals=globals())) # 0.02383529999997336
print(timeit.timeit('rec_fun_init(arr(300))', number=100, globals=globals())) # 0.03233700000009776

cProfile.run('rec_fun_init(arr(300))')

#          3232 function calls (2932 primitive calls) in 0.001 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       300    0.000    0.000    0.000    0.000 random.py:239(_randbelow_with_getrandbits)
#       300    0.000    0.000    0.001    0.000 random.py:292(randrange)
#       300    0.000    0.000    0.001    0.000 random.py:366(randint)
#         1    0.000    0.000    0.001    0.001 task_4_1.py:11(arr)
#         1    0.000    0.000    0.001    0.001 task_4_1.py:14(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_4_1.py:46(rec_fun_init)
#     301/1    0.000    0.000    0.000    0.000 task_4_1.py:55(recur_fun)
#       900    0.000    0.000    0.000    0.000 {built-in method _operator.index}
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       300    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       300    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
#       524    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# графики тут https://docs.google.com/spreadsheets/d/1JdlX_TU9nKyo-6lR1X9N5_KDL8SmYTV0K5esi9fPCXo/edit?usp=sharing