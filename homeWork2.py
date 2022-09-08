""" Задача 1

num = '10,56321'
num=num.replace(',','')
res = 0
i = 0
while i < len(num):
    num1=int(num[i])
    res = res + num1
    i += 1
print(res) 


Задача 2

from math import factorial

num=5
i=1
while i<=num :
  print (factorial(i))
  i+=1 
  
Задача 3

k = int(input('Введите число: '))
my_list = []

for i in range (1, k + 1):
    my_list.append(round((1 + 1/i)**i, 2))
print("Получившийся список: ", my_list)

summ = 0 
for j in my_list:
    summ = summ + j
print("Сумма элементов списка равна", summ)

Задача 4

n = int(input('Введите число: '))
array = []
result = 1

for i in range(-n, n + 1):
    array.append(i)
print(array)

num1 = int(input(f"Введите числа от 0 до {n * 2} через пробел: "))
num2 = int(input(f"Введите числа от 0 до {n * 2} через пробел: "))
for i in array:
    result = array[num1] * array[num2]
print("Произведение элементов на указанных позициях равно: ", result)


Задача 5

import random 

my_list=[1,3,2,4,5,6]
random.shuffle(my_list)
print(my_list) """


