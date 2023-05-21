year = int(input('year '))
if (year % 4 == 0 and year % 100 != 0):
    print ('YES')
elif year % 400 == 0:
    print ('YES')
else:
    print ('NO')
    
print("Год високосный" if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0) else "Год не високосный")

a = 'qwerty'
for i in a:
    print (i)

