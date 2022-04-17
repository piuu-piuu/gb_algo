#  Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

def merge_sort(arr):
    # print('input', arr)
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        return arr


if __name__ == '__main__':
    arr = [random.uniform(0.0, 50.0) for _ in range(10)] 
    print(arr)
    print(merge_sort(arr))
