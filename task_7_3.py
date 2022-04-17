# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. 
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
# Задача решена сортировкой "расческой" 
# Пример вывода:
# >>> Медиана массива [-85, -71, -68, -68, -23, -4, -1, 34, 38, 59, 78] равна -4.

import random

def next_gap(gap):
	gap = (gap * 10)/13
	if gap < 1:
		return 1
	return int(gap)

def comb_sort(arr):
	n = len(arr)
	gap = n
	swapped = True
	while gap !=1 or swapped == 1:
		gap = next_gap(gap)
		swapped = False
		for i in range(0, n-gap):
			if arr[i] > arr[i + gap]:
				arr[i], arr[i + gap]=arr[i + gap], arr[i]
				swapped = True

def median(arr):
    comb_sort(arr)
    return arr, arr[len(arr)//2]


if __name__ == '__main__':
    m=5
    arr = [random.randint(-100, 100) for _ in range(2*m+1)] 
    print(f'Медиана массива {median(arr)[0]} равна {median(arr)[1]}.')


