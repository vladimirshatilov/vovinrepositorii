print('enter 2 numbers')
a = int(input())
b = int(input())
pascal = 1
pascal = (b * 1000) + a
print(pascal)
#
print('enter a three-digit number')
a = input()
a = int(a)
ed = a // 100
a = a - ed*100
dec = a // 10
a = a - dec*10
sot = a // 1
a = a - sot*1
b = ed+dec+sot
print(b)
#
print('enter the number')
a = int(input())
a = a - (a // 10 - (a // 100)*10)*10
print(a)

