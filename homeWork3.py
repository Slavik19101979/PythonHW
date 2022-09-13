

# Задача 1,семинар 3
# my_list=[2, 3, 5, 9, 3]
# def summOdd(array):
#   res=0
#   for i in range(1,len(array),2):
#     res=array[i]+res
    
#   return res
# print(summOdd(my_list))

#Задача 2
# my_list=[2, 3, 5, 9,3]
# def multiplayOdd(array):
#   res=0
#   min,max=0,len(array)-1
#   while min<=max:
#     print(array[min]*array[max])
#     min+=1;max-=1
#   return -1
# multiplayOdd(my_list) 


# Задача 3
# my_list = [1.9, 0.2, 3.1, 10.01]
# def difrentFloat(array):
#   final_list=[] 
#   for i in array:
#     final_list.append(i-int(i))
#   print(round(max(final_list)-min(final_list),2))  
# difrentFloat(my_list)


# Задача 4
# num = int(input('Enter num: '))

# def binary(x):
#     result = ''
#     while x > 0:
#         result = str(x % 2) + result
#         x = x//2
#     return result

# print(binary(num))



# Задача 5
# num=int(input('enter num'))
# num2=-num
# def negoFibonacci(num):
#   if (num == 1) or (num == 2): return 1
#   else: return negoFibonacci(num+2)-negoFibonacci(num+1)

# def fibonacci(num):
#   if (num == 1) or (num == 2): return 1
#   else: return fibonacci(num-1)+fibonacci(num-2)

# my_list=[]
# for i in range(num2,1):
#   my_list.append(negoFibonacci(i))
# my_list2=[]
# for i in range(1,num+1):
#   my_list2.append(fibonacci(i))
  
# print(my_list+my_list2)





