print ('ввести длину бортиков')
N = int(input())
M = int(input())
print ('ввести расстояние до длинного бортика')
x = int(input())
print ('ввести расстояние до короткого бортика')
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
    print(y,"m")
else:
    print(x,"m")
    
