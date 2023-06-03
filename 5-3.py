def simple(num):
    for i in range (2, num-1):
        if num%i == 0:
            return False
    return True

m = int(input('Введите число M: '))
print(simple(m))