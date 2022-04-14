# 6.    Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанной программе из первых трех уроков. 
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
#  IDE VSCode 1.66.2
#  OC MS Windows [Version 10.0.19044.1620] x64
# 
# Исходная задача:
# В одномерном массиве найти сумму элементов, находящихся между 
# минимальным и максимальным элементами. Сами минимальный и максимальный элементы 
# в сумму не включать.
# 
# Проанализированы три алгоритма: c перебором, с сортировкой массива, с использованием встроенных min и max
# Самое большое потребление памяти у массива с сортировкой, т.к. сортировка на месте здесь невозможна 
# и приходится создавать новый массив. Самый экономный вариант - встроенные алгоритмы min/max.
# Пример :
# >>> Function minmax_fun, data size is 264 bytes.
# >>> Function run_fun, data size is 376 bytes.
# >>> Function sort_fun, data size is 416 bytes.

from random import randint
import sys

# очень хотелось решить задачу декоратором, и
# похоже, tracer это единственный способ.
# Несмотря на то, что функция это объект, другого доступа к ее локальным переменным "снаружи" не предусмотрено.
# Можно снаружи получить список имен локальных переменных, однако вне scope функциии они не возвращают значение/размер.
# поэтому использован подход известный как persistent locals. Добавил вычисление размеров переменных.

class persistent_locals(object):
    def __init__(self, func):
        # хранилище для locals декорируемой функции
        self._locals = {}
        self.func = func

    def __call__(self, *args, **kwargs):
        def tracer(frame, event, arg):
            # как только функция отработала, сохраняем себе ее Locals
            if event=='return':
                self._locals = frame.f_locals.copy()

        # подключаем tracer
        sys.setprofile(tracer)
        try:
            res = self.func(*args, **kwargs)
        finally:
            # убираем наш tracer
            sys.setprofile(None)
        return res

    def locals(self):
        # должна быть вызвана после выполнения функции,
        # возвращает имя функции и размер переменных
        l_size = 0
        for item in self._locals.values():
            l_size += sys.getsizeof(item)
        return self.func.__name__, l_size
    
# ниже - изучаемые функции 
# генератор списка
MIN = 1
MAX = 9
LIST_SIZE = 10
value_list = [randint(MIN, MAX) for _ in range(LIST_SIZE)]

@persistent_locals
def run_fun(value_list):
    min_i = max_i = 0
    min_e = max_e = value_list[0]
    for i, e in enumerate(value_list):
        if e < max_e:
            max_e = e
            max_i = i
        elif e > min_e:
            min_e = e
            min_i = i
    if max_i < min_i:
        max_i, min_i = min_i, max_i
    e_sum = 0
    for i in range(min_i+1, max_i):
        e_sum += value_list[i]
    return e_sum

@persistent_locals
def minmax_fun(value_list):
    max_i = value_list.index(max(value_list))
    min_i = value_list.index(min(value_list))
    e_sum = 0
    for i in range(min_i+1, max_i):
        e_sum += value_list[i]
    return e_sum

@persistent_locals
def sort_fun(value_list):
    sorted_list = sorted(value_list)
    max_i = value_list.index(sorted_list[-1])
    min_i = value_list.index(sorted_list[0])
    e_sum = 0
    for i in range(min_i+1, max_i):
        e_sum += value_list[i]
    return e_sum

# запускаем функции
minmax_fun(value_list)
run_fun(value_list)
sort_fun(value_list)

# собираем размеры переменных
print(f'Function {minmax_fun.locals()[0]}, data size is {minmax_fun.locals()[1]} bytes.')
print(f'Function {run_fun.locals()[0]}, data size is {run_fun.locals()[1]} bytes.')
print(f'Function {sort_fun.locals()[0]}, data size is {sort_fun.locals()[1]} bytes.')