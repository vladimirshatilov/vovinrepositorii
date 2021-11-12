print ('enter amount of apples')
k = int(input())
print ('enter amount of pupils')
n = int(input())
print ('there are',k%n,'apples in the basket')
#
print('enter minutes')
n = int(input())
hours = n // 60
mins = n % 60
if hours >= 24:
    hours -=24
print ('Time is:',hours,'hours',mins,'mins',sep=' ')
#
print ('enter year')
n = int(input())
if ((n%10 == 4) and (n%100 == 0)) or(n%1000 == 400):
                   print('YES')
else:
    print('NO')
#
#
print ('enter 3 numbers')
a = int(input())
b = int(input())
c = int(input())

if (a<b) and (a<c):
    print (a)
elif (b<c) and (b<a):
    print (b)
elif (c<b) and (c<b):
    print (c)
#
#
print ('enter the starting cell')
str1 = int(input())
stol1 = int(input())
print ('enter the end cell')
stol2 = int(input())
str2 = int(input())

if ((str1 == str2) and (stol1 != stol2)) or ((stol1 == stol2) and (str1 != str2)):
    print('YES')
else:
        print('NO')
#
#
print ('enter the lenght of edge')
N = int(input())
M = int(input())
print ('enter the distance to the long edge')
x = int(input())
print ('enter the distance to the short edge')
y = int(input())

if M>N:
    long = M
    short = N
else:
    long = N
    short = M

if x > long//2:
    x = long - x

if y > short//2:
    y = short - y

if x>y:
    print(y)
else:
    print(x)
