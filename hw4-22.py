# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

lst1 = []
n = int(input('N: '))
lst2 = []
m = int(input('M: '))

for i in range(n):
    lst1.append(random.randint(0, 10)) # или lst1.append(int(input('n: ')))
print(lst1)

for i in range(m):
    lst2.append(random.randint(0, 10)) # или lst2.append(int(input('m: ')))
print(lst2)

print(sorted(set((lst1)).intersection(set(lst2))))