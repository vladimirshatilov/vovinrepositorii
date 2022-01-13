print ('ввести номер столбца')
m = int(input())
print ('ввести номер строки')
n = int(input())

if (m>8) or (n>8) or (n<0) or (m<0):
    print('Stack overflow')



if m%2 == n%2 :
    print ('белая')
else:
        print ('чёрная')
        
