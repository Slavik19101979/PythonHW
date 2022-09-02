
# Задача 1
""" from cmath import sqrt

x1 = int(input('x1 -->'))
y1 = int(input('y1 -->'))
x2 = int(input('x2 -->'))
y2 = int(input('y2 -->'))
result = sqrt((x2 - x1)** 2 +(y2 -y1) ** 2)
result = round(float(result.real),2)
print(f"Расстояние между точками: {result} м") """


# Задача 2

""" num = int(input('Введите номер четверти: '))
if num == 1:
    print('x > 0 and y > 0')
elif num == 2:
    print('x < 0 and y > 0')
elif num == 3:
    print('x < 0 and y < 0')
elif num == 4:
    print('x > 0 and y < 0')
else:
    print('Don\'t do stupid things!') """
    
# Задача 3

""" x = int(input('x -->'))
y = int(input('y -->'))

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
else:
    print('X и Y не должны быть равны нулю') """
    

# Задача 4
 
num = int(input('Введите день недели: '))
if 1 <= num <= 5:
    print('This is work day')
elif num == 6 or num == 7:
    print('This is holiday')
else:
    print('Incorrect input') 