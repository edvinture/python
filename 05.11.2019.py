# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:08:22 2019

@author: user
"""

print ("Привет хочу что-нибудь купить!")
tovar1 = float(input("\nСтоимость первого товара = "))
tovar2 = float(input("\nСтоимость второго товара = "))
if tovar1 + tovar2 > 100 :
    print ("\n Сума денег не достаточна ") 
else:
    print ("\n Чек оплачен, повезло скидки!")
print ("Пока")
     
import random
rnd=random.randint(1,20)
print(rnd)

rnd2=random.randrange(10,20,2)
print(rnd2)

print (random.random())

print(random.choice('abcdef'))

print (random.sample(range(50),10)) #Выбирает 10 элементов из списка 50

a=float(input("сторона а: "))
b=float(input("сторона b: "))
if a==b:
    print("Квадрат")
else:
    print("Не квадрат")
    
a=float(input("Первое число: "))
b=float(input("Второе число: "))
operation = input ("Выберите действие:")
if operation == "+":
    print ("a+b=",a+b)
elif operation == "*":
    print ("a*b=",a*b)
elif operation == "-":
    print ("a-b=",a-b)
elif operation == "/":
    print ("a/b=",a/b)
else:
    print ("Неверное действие")

bd=int(input("Год рождения:"))
today=int(input("Сегодняшний год:"))
if (today-bd)%10==0:
    print ("Юбилей")
else:
    print ("Не в этом году")

price=float(input("Цена товара:"))
if  price<10:
    print ("Цена со скидкой 10%:",price*0.9)
else:
    print ("Цена со скидкой 20%:",price*0.8)









