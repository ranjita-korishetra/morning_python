
import calendar
year=int(input('enter the year:'))
month=int(input('enter the month:'))
display = calendar.month(year,month)
print(display)


import datetime
print(datetime.datetime.now())

import math
print(math.factorial(6))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(6))

import math
print(f"{6}!=", " × ".join(map(str, range(6, 0, -1))), "=", math.factorial(6))

num=int(input('enter the number whose factorial has to be found:'))
fact=num
for i in range(1,num):
    fact = fact * 1
print('factorial of',num,'is',fact)


base = float(input("Enter the base of triangle: "))
height = float(input("Enter the height of triangle: "))
area = 1/2*base*height
print("The area of the triangle is:", area)

miles=int(input('enter the miles:'))
kilometers= miles*1.6
print(f'{miles} miles equal to {kilometers} kilometers')

a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
temp = a
a = b
b = temp
print("After swapping:")
print("a =", a)
print("b =", b)

num = float(input('Enter a number:'))
if num > 0:
    print('The number is Positive.')
elif num < 0:
    print('The number is Negative.')
else:
    print('The number is Zero.')