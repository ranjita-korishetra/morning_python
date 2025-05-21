
print("hello python")

num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))
sum_result=num1 + num2
div_result=num1 / num2
print(f'sum:{num1}+{num2}={sum_result}')
print(f'div:{num1}/{num2}={div_result}')


base=int(input('enter the base of the triangle:'))
height=int(input('enter the height of the triangle:'))
area=1/2*base*height
print(f'the area of the triangle is:{area}')
'''
'''
a = input('enter the first variable(a):')
b = input('enter the second number(b):')
temp=a
a=b
b=temp
print(f'swapped values:a={a},b={b}')


a=input('enter the first variable(a):')
b = input('enter the second number(b):')
a,b=b,a
print('after swapping:')
print("a=",a)
print("b=",b)


num=int(input('enter the number:'))
if num>0:
    print('positive number')
elif num==0:
    print('zero')
else:
    print('negative number')


miles=float(input('enter the miles:'))
kilometer=miles*1.6
print(f'{miles} miles equal to {kilometer}kilometer')

celsius =float(input('enter the celsius:'))
fahrenheit =(celsius*9/5)+32
print(f'{celsius}degrees celsius is equal to{fahrenheit} ')


x=list(range(0,101,2))
print(x)

x=[]
for i in range(0,101,2):
    print(i)


li= [1,5,6,8,3]
y = []
for i in range(len(li)):
    if i % 2 == 1:
        y.append(li[i]**2)
print(y)

li= [1,5,6,8,3]
y=[li[i]**2 for i in range(len(li)) if i%2==1]
print(y)
z=[li[i]*5 for i in range(len(li)) if i%2==1]
print(z)
k=[i* 2 for i in li]
print(k)

li=[11,3,6,10,13]
y = []
for i in range(5):
    if li[i] % 3==0:
        y.append(li[i]**2)
print(y)

z=[]
for i in range(5):
    z.append(li[i]+5)
print(z)

li=[11,3,6,10,13]
y=[li[i]**2 for i in range(len(li)) if i%2==1]
print(y)
z=[li[i]*5 for i in range(len(li)) if i%2==1]
print(z)
k=[i* 2 for i in li]
print(k)



x=['hi','python','we','write','python','we','say','hi','python']
y={}
for i in x:
    if i in y.keys():
        y[i]=y[i]+1
    else:
        y[i]=1
print(y)

x=[('a',10),('b',20),('c',30),('d',40)]
for i in x:
    print(i[1],end =' ')


x=['a','b','c','d']
y=[10,20,30,40]
z={}
for i in range(len(x)):
    z[x[i]]=y[i]
print(z)

x=['a','b','c','d']
y=[10,20,30,40]
z=[(x[i],y[i]) for i in range(len(x))]
print(z)


x=10
def f1():
    x=20
    print(x)
    print(globals()['x'])
f1()

x=10
y=20
def f1():
    y=30
    print(x)
    print(y)
    print(globals()['x'])
    print(globals()['y'])
f1()

num = int(input("display multiplication table of:"))

for i in range(1,11):
    print(f"{num}x{i}={num*i}")
'''
'''
x=int(input('enter the year:'))
if x<5:
    print(" bus pass is free")
elif x>=60:
    print(" senior citizen discount")
else:
    print("pay the full price")

x=int(input('enter the meal time:'))
if x==8:
    print('its breakfast time')
elif x==1:
    print('its lunch time')
elif x==20:
    print('its dinner time')
else:
    print('its not meal time')


i=1
while i<=5:
    print(i)
    i+=1


name= ('ranju','hari','kori','chanagowdra')
print(name[0])
print(name[1])
print(name[3])
print(name[-2:])
print(name)

my_list=list(range(13))
print(my_list)

one=('ranjita')
two=set(one)
print(two)

di={
    'name':'ranjita',
    'address': 'bkt',
    'number':6361
}
print(di['name'])

di={
    'ename':'hari',
    'esal':3000
}
di['esal']=5000
print(di)

def f1(x,y):
    print(x+y)
f1(10,20)

def f2(x):
    if x%2==0:
        return'even'
    else:
        return'odd'
result=f2(5)
print(result)

class Details:
    x=10
    def m1(self):
        print('Hello')

