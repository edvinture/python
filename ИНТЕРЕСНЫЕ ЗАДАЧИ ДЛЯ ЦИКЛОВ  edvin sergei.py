# Edvin Kääpa, Sergei Smirnov sptvr19

#1
x = 1000
while True:
    print(x)
    x +=3
    if x == 1018:
        break
    
#2
x = 1
while True:
    print(x)
    x +=2
    if x == 113:
        break
    
#3
x = 90
while True:
    print(x)
    x -=5
    if x == -5:
        break
        
#4
x = 2
while True:
    print(x)
    x *=2
    if x >= 2097152:
        break

#5
a = 2
while a < 9999:
    print(a)
    a = 2*a-1
    
#6
a=-166
while a<100:
    if -100<a<-9 or 9<a<100:
        print(a)
    a=2*(a-1)+200
    
#7
n = int(input("Введите число"))
x = 1
sum = 1
for x in range(1,n+1):
    sum *= x
    x += 1
print(sum)
#8
x = int(input())
for i in  range(1,x+1):
    if (x%i==0):
        print(i)
        
#9
n = int(input())
x = int((n**(1/2))//1)
us = False
for i in range(2,x):
    if x%i == 0:
        us = True
if us== True:
    print("составное")
else:
    print("простое")

    
    