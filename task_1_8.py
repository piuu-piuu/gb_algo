# 8. Определить, является ли год, который ввел пользователь, 
# високосным или не високосным.

year = int(input('Введите год: '))

if year % 400 == 0:
    year_type = 'високосный'
elif year % 100 == 0:
    year_type = ' невисокосный'
elif year % 4 == 0:
    year_type = 'високосный'
else:
    year_type = 'невисокосный'

print('Год', year_type)