# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# Пример:
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

lst = []
n = int(input('N: '))

for i in range(n):
    lst.append(i+1)
    # lst.append(random.randint(0, 10))
print(lst)
x = int(input('X = '))
result = 0
count = 0

for i in range(n):
    # print(lst[i])
    if (x-1 == lst[i]) or (x+1 == lst[i]):
        result = lst[i]
    elif (x-2 == lst[i]) or (x+2 == lst[i]):
        result = lst[i]
    elif (x-3 == lst[i]) or (x+3 == lst[i]):
        result = lst[i]

print(result)