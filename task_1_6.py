# 6. Пользователь вводит номер буквы в алфавите. 
# Определить, какая это буква.

num = int(input('Введите число: '))
pos = ord('`') + num
letter = chr(pos)
print(letter)