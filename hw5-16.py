# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N 
# – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

import random

lst = []
n = int(input('N: '))
for i in range(n):
    lst.append(random.randint(0, 10))
print(lst)
x = int(input('X = '))
count = 0
for i in range(n):
    if lst[i] == x:
        count += 1
print('Число', x, 'встречается в списке', count, 'раз')
