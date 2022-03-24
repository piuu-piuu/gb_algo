# В диапазоне натуральных чисел от 2 до 99 определить, 
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9

VALUE_MIN = 2
VALUE_MAX = 99
DIVIDER_MIN = 2
DIVIDER_MAX = 9
SHIFT = 2

div_counter = [0 for _ in range(DIVIDER_MAX - DIVIDER_MIN + 1)]
for y in range(DIVIDER_MIN, DIVIDER_MAX + 1):
    pos = 0
    while pos < VALUE_MAX:
        pos +=y
        div_counter[y - SHIFT] += 1
print(div_counter)