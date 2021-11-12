
print ('enter the values of the list, ending with zero')
A = [1]
S = 0 
i = -1
buff = 1
while buff != 0:
    i +=1
    A.insert(i,(buff))
    buff = int(input())
A.remove(1)
A.pop(len(A)-1)

def srar(A):
    S = 0
    for i in range(len(A)):
        S += A[i]
    return S/len(A)

print(A)
print(srar(A))
#
def bin(a):
    i = 0
    binar = ['1']
    while a>1:
        binar.append(str(a%2))
        a = a//2
        i += 1
    return("".join(binar))

def dec(b):
    i = 0
    decim = 0
    while len(b)!=0:
        decim += (int(b)%10)*(2**i)
        b = b[:(len(b)-1)]
        i += 1
    return(decim)


print('enter the number in decimal')

a = int(input())
print('same in binary:',bin(a))

print('enter the number in binary')

b = str(input())
print('same in decimal:',dec(b))
#
print('enter years')
years = int(input())

print('enter money')
a = int(input())

def bank(years,a):
    i = 0
    for i in range (years):
        a += 0.1*a
    return (a)

print(bank(years,a))
#
#
print('coordinates)

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())



def distance(x1,x2,y1,y2):
    X = abs(x1-x2)
    Y = abs(y1-y2)
    S = (X*X+Y*Y)**0.5
    return(S)

print(distance(x1,x2,y1,y2))
#
#
print ('enter the number and the degree to which you want to raise it')

a = int(input())
n = int(input())

def power(a,n):
    m = a
    for i in range(n):
            a *= m
    if n>0:
        return (a)
    elif n<0:
        return (1/a)
    elif n == 1:
        return (1)

print(power(a,n))
#
#
print ('enter the number')
a = int(input())

def is_prime(a):
    for i in range (2,1000):
        if a%i != 0:
            return True
            break
        else:
            return False
           

print (is_prime(a))
#
