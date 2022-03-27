# Написать два алгоритма нахождения i-го по счёту простого числа. 
# Функция нахождения простого числа должна принимать на вход натуральное 
# и возвращать соответствующее простое число. 
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. 
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import cProfile
import timeit
import math


def sieve(prime_count):
    SEGMENT_SIZE = 10000
    segment = [0] * SEGMENT_SIZE
    # все чётные числа сразу оставляем вычеркнутыми
    for i in range(1,SEGMENT_SIZE,2):
        segment[i] = i 
    # вторым элементом является единица, которую не считают простым числом
    # - вычеркиваем
    segment[1] = 0
    # возвращаем единственный чётный prime
    segment[2] = 2 
    number = 2 # замена на 0 начинается с 3-го элемента (первые два уже нули)
    # Для максимального числа данного диапазона: если существует
    # делитель больше корня этого числа, значит существует соответствующий ему
    # делитель меньше корня. Т.е. поиск делителей можно ограничить корнем из  
    # максимального числа данного диапазона
    while number < round(math.sqrt(SEGMENT_SIZE)): 
        if segment[number] != 0: # если он не равен нулю, то это prime
            sieve_hole = number + number # текущая позиция num, дальше перемещаемся с шагом num
            while sieve_hole < SEGMENT_SIZE:
                segment[sieve_hole] = 0 # заменить на 0
                sieve_hole = sieve_hole + number # перейти в позицию на num больше
        number += 1
    primes = []
    for i in segment:
        if segment[i] != 0:
            primes.append(segment[i])
    del segment
    return primes[prime_count]




def prime(prime_count):
    if prime_count == 0:
        return 2   
    if prime_count == 1:
        return 3   
    num = 3
    while prime_count > 1:
        num +=1
        isPrime = True
        for y in range(2, num):
            if num%y == 0:
                isPrime = False
                break      
        if isPrime == True:
            prime_count -= 1
    return num

print(sieve(1200))
print(prime(1200))

print(timeit.timeit('sieve(10)', number=100, globals=globals()))  # 0.14656580000882968
print(timeit.timeit('sieve(50)', number=100, globals=globals()))  # 0.14665890001924708
print(timeit.timeit('sieve(100)', number=100, globals=globals())) # 0.14573240000754595
print(timeit.timeit('sieve(200)', number=100, globals=globals())) # 0.14760900000692345
print(timeit.timeit('sieve(400)', number=100, globals=globals())) # 0.1462941000063438
print(timeit.timeit('sieve(800)', number=100, globals=globals())) # 0.1473618999880273
print(timeit.timeit('sieve(1200)', number=100, globals=globals()))# 0.1442953999794554

cProfile.run('sieve(1200)')
#    1431 function calls in 0.002 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 task_4_2.py:16(sieve)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#        99    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#        99    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#      1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


print(timeit.timeit('prime(10)', number=100, globals=globals()))   # 0.001141099986853078
print(timeit.timeit('prime(50)', number=100, globals=globals()))   # 0.02991969999857247
print(timeit.timeit('prime(100)', number=100, globals=globals()))  # 0.09921799998846836
print(timeit.timeit('prime(200)', number=100, globals=globals()))  # 0.4443637000222225
print(timeit.timeit('prime(400)', number=100, globals=globals()))  # 2.0815646999981254
print(timeit.timeit('prime(800)', number=100, globals=globals()))  # 9.683184499997878
print(timeit.timeit('prime(1200)', number=100, globals=globals())) # 23.899930400017183

cProfile.run('prime(1200)')
#    4 function calls in 0.263 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.263    0.263 <string>:1(<module>)
#         1    0.263    0.263    0.263    0.263 task_4_2.py:49(prime)
#         1    0.000    0.000    0.263    0.263 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Графики:    
# https://docs.google.com/spreadsheets/d/1fusWDqPFlptLMpgeNL4mqHt1rKz1BPujgDkQW84B3XY/edit?usp=sharing








