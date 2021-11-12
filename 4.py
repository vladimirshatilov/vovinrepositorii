print ('enter coefficients of quadratic equation a,b,c.')
a = int(input())
b = int(input())
c = int(input())

import math

D = math.sqrt(b*b - 4*a*c)

print(D)
#
#
print ('enter N')
N = int(input())

i = 1

while i*i <= N:
    print(i*i)
    i += 1
#
#
print ('enter the number')
n = int(input())
i = n//2
nnd = 0
for i in range(n//2,2,-1):
    if (n%i == 0):
        nnd = i
        
print (nnd)
#
#
  
print ('enter the number')
n = int(input())
fib = [0]*(n+1)
fib[1] = 1 
for i in range(1,n+1):
    fib[i] = fib[i-1] + fib[i-2]
    fib[1] = 1
    print (fib[i])

print (fib[n])
#
#
print ('enter the lenght of list')
n = int(input())
A = ['']*n

for i in range (n):
    A[i]=str(input())

for i in range (n):
    if i%2 == 0:
        print(A[i])
#
#
print ('enter the lenght of list')
n = int(input())
A = ['']*n

for i in range (n):
    A[i]=int(input())

for i in range (n):
    if A[i]%2 == 0:
        print(A[i])
#
#
print ('enter the lenght of the array')
n = int(input())
A = [0]*(n+1)
print ('enter a list of numbers with signs + and -')

for i in range (n):
    A[i] = int(input())

for i in range (n):
    if (A[i]>=0 and A[i+1]>=0) or (A[i]<0 and A[i+1]<0):
        print(A[i],A[i+1])
        break
#
#
print ('enter the sequence, ending with zero')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

print('objects, neighbors:')

for i in range (1,(len(A)-2)):
    if (A[i]>A[i-1]) and (A[i]>A[i+1]):
        S += 1
        

print(S)
#
#
print ('enter the heigh values of all students, ending with zero')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

print ('enter high')
X = int(input())

sorted(A) #удобно

for i in range (len(A)):
    if A[i]<X:
        print(X)
        break
#
#
print ('enter the values in ascending order, ending with zero')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

for i in range(len(A)):
               if A[i] != A[i-1]:
                   S += 1

print (S-2)
#
#
print ('enter the values, ending with zero')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

imax = 0
maxi = 0

for i in range(len(A)):
    if A[i]>maxi:
        maxi = A[i]
        imax = i

print (maxi,' ',imax)
#
#
print ('enter the values, ending with zero')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

imax = 0
maxi = 0

for i in range(len(A)):
    if A[i]>maxi:
        maxi = A[i]
        imax = i

print (maxi,' ',imax)
#
#
print ('enter the values, ending with zero')
A = [1]
S = 0 
i = 0
while A[i] != 0:
    i +=1
    A.insert(i,(int(input())))

maxi = 0

for i in range(len(A)):
    if A[i] == A[i-1]:
        S += 1
    else:
        if S> maxi:
            maxi = S
        S = 0

print (maxi+1)
#
#
print ('enter the numbers of the first list, ending with zero')
A = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    A.insert(i,(buff))
    buff = int(input())
    



print ('enter the numbers of second list, ending with zero')
B = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    B.insert(i,(buff))
    buff = int(input())

A.remove(1)
B.remove(1)

C = [1]
if len(A) == len(B):
    for i in range (len(A)):
        C.insert(i,(A[i] + B[i]))

C.remove(1)
#
#
print ('enter the values of the first list, ending with zero')
A = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    A.insert(i,(buff))
    buff = int(input())
    



print ('enter the values of the second list, ending with zero')
B = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    B.insert(i,(buff))
    buff = int(input())

A.remove(1)
B.remove(1)

Sum = 0
C = [1]

if len(A) == len(B):
    for i in range (len(A)):
        Sum += A[i]*B[i]

print(Sum-1)
C.remove(2)
print(C)


