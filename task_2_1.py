# 1. Написать программу, которая будет складывать, вычитать, 
# умножать или делить два числа. Числа и знак операции вводятся 
# пользователем. После выполнения вычисления программа не 
# завершается, а запрашивает новые данные для вычислений. 
# Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак
# (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке
# и снова запрашивать знак операции. Также она должна сообщать
# пользователю о невозможности деления на ноль,
# если он ввел его в качестве делителя.

def operation(x,y):
    operator = input('operator: ')
    if operator == '0':
        print('Конец работы')
        return 'end'
    if operator == '+': 
        print(x + y)
    elif  operator == '-':
        print(x - y)
    elif  operator == '*':
        print(x * y)
    elif  operator == '/':
        if y == 0:
            print('Division by zero')
        else:
            print(x / y)
    else:
        print('Wrong operator')
        operation(x,y)

def recur_fun():
    _x = int(input('value 1: '))
    _y = int(input('value 2: '))
    if operation(_x,_y) == 'end':
        return None
    return recur_fun()

recur_fun()