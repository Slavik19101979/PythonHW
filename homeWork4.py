# Задача 1. Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141

# def round_pi(x):
#     n = len(d)-2
#     return round(pi, n)

# d = (input('Введите число: '))
# print(round_pi(d))

#Задача 2.Множители

# num1 = int(input('Введите  число: '))
# def find_div(n):
#     dividers = []
#     for i in range(2, n + 1):
#         while n % i == 0:
#             n //= i
#             dividers.append(i)
#     return dividers
# print(find_div(num1))

#Задача 3

# array=[1, 1, 2, 3, 4, 5, 5] 
# new_array=[]
# for i in array:
#     if array.count(i) == 1:
#         new_array.append(i)           
# print (new_array)

#Задача 4
# from random import randint


# randint
# def equ(k):
#     randList = [randint(0,100)]
#     result = str(randList[0])
#     for counter in range(1,k+1):
#         randList.append(randint(0,100))
#         result = f'{randList[-1]}*x^{counter} + '+ result   
#     result = result.replace('x^1 ','x ') 
#     result = result.replace(' + 0','') 
#     result = result.replace(' 1*',' ')
#     return result

# k = int(input("Введите степень: "))
# print(equ(k))

# with open('mnogochlen.txt', 'w+') as t:
#     t.write(equ(k))

#Задача 5
# data=open("1.txt","r")
# array=data.read()
# data_1=open('2.txt','r')
# array_1=data_1.read()
# result=sum(map(int,array.split()))+sum(map(int,array_1.split()))

# with open('result.txt','w') as rr:
#     rr.write(str(result))




