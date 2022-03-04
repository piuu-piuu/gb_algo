# 5. Пользователь вводит две буквы. Определить, на каких местах
#  алфавита они стоят, и сколько между ними находится букв.

a,b = input('Введите через пробел две буквы: ').split(' ')
_base = ord('`')
num_a = ord(a)
num_b = ord(b)
pos_a = num_a - _base
pos_b = num_b - _base
between_ab = abs(pos_a-pos_b) -1

print(f'Буквы {a} и {b} занимают {pos_a} и {pos_b} места в алфавите')
print(f'Букв между ними {between_ab}')