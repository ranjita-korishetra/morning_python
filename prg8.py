
class Details:
    x=10
    def m1(self):
        print('Hello')
d = Details()
print(d.x)
d.m1()

name=input('enter the name:')
age=input('enter the age:')
location=input('enter the location:')
class PersonalDetails:
    def display_details(self,name,age,location):
        print('name is',name)
        print('age is',age )
        print('location is',location)
p= PersonalDetails()
p.display_details(name,age,location)


x=int(input('enter the first number:'))
y=int(input('enter the second number:'))
class MathOperations:
    def sum(self,x,y):
        print('the sum of',x,'and',y, x+y)
    def sub(self,x,y):
        print('the sub of',x,'and',y, x-y)
    def product(self,x,y):
        print('the product of',x,'and',y, x*y)
    def quotient(self,x,y):
        print('the quotient of',x,'and',y, x//y)
M=MathOperations()
M.sum(x,y)
M.sub(x,y)
M.product(x,y)
M.quotient(x,y)


z=30
class A:
    y=20
    def m1(self):
        x=10
        print(x)
        print(A.y)
print(z)
print(A.y)
a=A()
a.m1()

# 1. assume that your writing a python application for a training institute.
#2. come upwith at least 4 classes where each class will have 2 method

class Institute:
    def college(self):
        print('my college stjit')
    def course(self):
        print('i want do python course')
class Details:
    def name(self):
        print('my name is ranjita')
    def address(self):
        print('i am from ranebennur')
I = Institute()
I.college()
I.course()
D=Details()
D.name()
D.address()

class Info:
    def __init__(self,id,name,course):
     print('id is',id)
     print('name is',name)
     print('course is',course)
    def m2(self):
        print('self.id')
        print('self.name')
        print('self.course')

a=Info(12,'xyz','python')
a.m2()
b=Info(13,"ranjita",'java')
b.m2()
c=Info(14,'sneha','ds')
c.m2()

class Mathoperations:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def  add(self):
        print(self.num1+self.num2)
    def sub(self):
        print(self.num1-self.num2)
    def mul(self):
        print(self.num1*self.num2)
    def div(self):
        print(self.num1/self.num2)
a=Mathoperations(2,3)
a.add()
b=Mathoperations(2,3)
a.sub()
c=Mathoperations(2,3)
a.mul()
d=Mathoperations(2,3)
d.div()

# create a studentclass with init and display methods.
# init method should have 3 parameters no,name,sub to initialize student object with values.
#display method should display student details.
#nowcreate 3student objects with below values.
#also display each student details with corresponding objects

class Student:
    def __init__(self,no,name,sub):
     print('no','=',no)
     print('name','=',name)
     print('sub','=',sub)
    def display(self,no,name,sub):
        print('no','=',no)
        print('name','=',name)
        print('sub','=',sub)

S=Student(12,'ranjita','python')
S.display(13,'priya','java')

class Student:
    def __init__(self,no,name,sub):
     self.no=no
     self.name=name
     self.sub=sub
    def display(self):
        print('number','=',self.no)
        print('name','=',self.name)
        print('sub','=',self.sub)

s=Student(1,'ranjita','python')
s.display()

#call arguments in another method using self variables
class Student:
    def __init__(self,no,name,sub):
        self.no = no
        self.name = name
        self.sub = sub
    def display(self):
        print('no','=',self.no)
        print('name','=',self.name)
        print('sub','=',self.sub)

S=Student(1,'ramesh','python')
S.display()
t=Student(2,'suresh','django')
t.display()
u=Student(3,'ranjita','java')
u.display()


z=40
class Info:
    y=30
    x=20
    print(z)
    def m1(self):
        self.y=20
        print(self.y)
i=Info()
i.m1()


class TypesMethods:
    def __init__(self):
        print('init method')
    def instance(self):
        print('Instance method')
    def class_method(self):
        print('class method')
    def static_method(self):
        print('static method')
t=TypesMethods()
t.instance()
t.class_method()
t.static_method()

class Assignment:
    x=10
    y=20
    def method_one(self,x):
        self.z=30
        print(Assignment.x)
        print(Assignment.y)
        print(self.z)
    @classmethod
    def method_two(cls,y):
        print(y)
        print(Assignment.x)
        print(Assignment.y)

a=Assignment()
a.method_one(50)
a.method_two(50)



