'''
s=input('enter a string:')
def st(s):
    print(s[::-1])
st(s)
'''
'''

num1=int(input('enter first number:'))
num2=int(input('enter the second number:'))
def sum(num1,num2):
    return f'sum of {num1} and {num2} is {num1+num2}'
pr2=sum(num1,num2)
print(pr2)
'''
'''
s=input('enter a string:')
def st(s):
    return s[::-1]
pr3=st(s)
print(pr3)
'''
'''
x=int(input('enter the first number:'))
y=int(input('enter the second number:'))
z=int(input('enter the third number:'))
if x>y:
    if x>z:
        print(x,'is biggest among',y,'and',z)
    else:
        print(z, 'is biggest among', x, 'and',y)
else:
     if y>z:
        print(y,'is biggest among',x,'and',z)
     else:
        print(z,'is biggest among',x,'and',y)
        '''

