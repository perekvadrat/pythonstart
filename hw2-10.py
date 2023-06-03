# Задача 10: 
# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 

# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.

# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input('Количество монет: '))
count0 = 0
count1 = 0

for i in range(n):
    rub = random.randint(0, 1)
    print(rub)
    if rub == 0:
        count0 += 1
    else:
        count1 += 1

if (count0 <= count1):
    print('Перевернуть орлов: ') 
    print(count0)
else:
    print('Перевернуть решек: ') 
    print(count1)