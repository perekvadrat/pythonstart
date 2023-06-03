# fib1 = 1
# fib2 = 1
 
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
 
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i += 1
 
# print("Значение этого элемента:", fib2)

def fib(n):
    if n == 0:
        return 0
    elif n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
m = int(input('Введите число M: '))
    
print(fib(m))
