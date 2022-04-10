# Пользователь вводит данные о количестве предприятий, их наименования 
# и прибыль за 4 квартала (т.е. 4 числа) для каждого предприятия. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) 
# и отдельно вывести наименования предприятий, 
# чья прибыль выше среднего и ниже среднего.

from collections import Counter

total_businesses = int(input())
profits = Counter()
for i in range(total_businesses):
    business = input()
    for j in range(4):
        n = input()
        if n.isdigit:
            profits[business] += int(n)
avg = sum(profits.values()) / total_businesses
print('\nприбыльные: ', end = ' ')
for firm, profit in profits.items():
    if profit > avg:
        print(firm, end = ' ')
print('\n----------------------')
print('убыточные: ', end = ' ')
for firm, profit in profits.items():
    if profit < avg:
        print(firm, end = ' ')