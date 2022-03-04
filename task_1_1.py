# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

value = int(input('Введите трёхзначное число: '));
hundreds = value //100
tens = (value % 100) //10
ones = value % 10
 
sum = hundreds + tens + ones 
product = hundreds * tens * ones

print('Сумма цифр: ', sum)
print('Произведение цифр: ', product)