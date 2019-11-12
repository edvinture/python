1#
try:
     k = 1 / 0
except ZeroDivisionError:    
     k = 0
print(k)
0

#2
try:
     k = 1 / 0
except ArithmeticError:
     k = 0
print(k)
0

#3

f = open('1.txt')
ints = []
try:
    for line in f:
         ints.append(int(line))
except ValueError:
     print('Это не число. Выходим.')
except Exception:
     print('Это что ещё такое?')
else:
     print('Всё хорошо.')
finally:
     f.close()
     print('Я закрыл файл.')
     # Именно в таком порядке: try, группа except, затем else, и только потом finally.
