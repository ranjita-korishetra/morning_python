''''
#13/3/25
#single level
class A:
    x=10
class B(A):
    y=20
a=A()
print(a.x)
b=B()
print(b.y)
print(b.x)

#multilevel
class A:
    x=10
class B(A):
    y=20
class C(B):
    z=30
a=A()
print(a.x)
b=B()
print(b.y)
print(b.x)
c=C()
print(c.z)
print(c.x)
print(c.y)

#hierarchical
class A:
    x=10
class B(A):
    y=20
class C(A):
    z=30
b=B()
print(b.y)
print(b.x)
c=C()
print(c.z)
print(c.x)

#multiplelevel
class A:
    x=10
class B:
    y=20
class C(A,B):
    z=30
c=C()
print(c.z)
print(c.x)
print(c.y)

#hybrid/diamond
class A:
    x=10
    y=20
class B(A):
    z=30
class C(A):
    k=40
class D(B,C):
    print('Hybrid or Diamond')
d=D()
print(d.x)
print(d.y)
print(d.z)
print(d.k)

class A:
    def __init_(self):
        print('hi')
class B(A):
    def __init__(self):
        super().__init__()
        print('hello')
b=B()

#implement a student grading system.create a class student with following
# A constructor to initialize the student's name,rool number,and marks in three subjects.
# A method calculate_avrage() to calculate the avg marks.
#A method display_grade()to display the grade based on the avg marks:
# A FOR AVG>=90
# B FOR AVG>=75 AND <90
# C FOR AVG>=50 AND <75
# D FOR AVG<50

class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def calculate_average(self):
        return sum(self.marks)/len(self.marks)
    def display_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            grade='A+'
        elif avg >=75:
            grade='A'
        elif avg >=50:
            grade='B'
        else:
            grade='C'
        print(f'Student:{self.name},roll number:{self.roll_number},Average Marks: {avg:.2f}, Grade: {grade}')

s1=Student('ranjita',1,[20,30])
s1.display_grade()
s2=Student('priya',2,[15,20])
s2.display_grade()


#implement a banking system.create a class bankaccount that simulates asimple banking system.implment the following:
# A method deposite(ammount)to add money to the account
#A method withdraw(ammount)+withdraw money the balance
#  A method display_blance()diplay cuurent balance.
class BankAccount:
    def __init__(self,holder_name,account_number,balance):
        self.holder_name=holder_name
        self.account_number=account_number
        self.balance=balance
    def deposite(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print('deposit amount must be positive')

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")
    def display_balance(self):
        print(f"Account Holder: {self.holder_name}, Balance: {self.balance}")
account1 = BankAccount("ranjita", "Alice", 1000)
account1.deposite(500)
account1.withdraw(300)
account1.display_balance()
'''
'''
#14/3/25
#Exception
#1
li=[10,20,30,40,50]
x=10
try:
    print(x/2)
    print(li[3])
    print(10/0)
except Exception as e:
    print(e)
except:
    print('an error occurred')
print('hello')

#2
x=int(input('please enter a number:'))
try:
    print(x)
    y=[10,20,30]
    print(y[0])
    print(y[1])
    print(y[2])
    print(y[3])
except Exception as e:
    print(e)

#3
print('good morning')
x=10
li =[1,2,3,4,5]
try:
    print(x/0)
except Exception as e:
    print(e)
try:
    print(li[5])
except Exception as e:
    print(e)

#4
x=[10,20,30,40,50]
y=10
try:
    print(x[0])
    print(y/0)
except IndexError:
    print('Trying to access a non existent index')
except ZeroDivisionError:
    print('trying to divide a number by 0')
except:
    print('An error occurred')

#file
f=open('sample.txt','w')
f.write('this is file operation')
f.close()
f=open('sample.txt','a')
f.write('\n welcome to python')
f.close()
f=open('sample.txt','r')
res = f.readline() #reading a oneline
print(res)

#create a file named Info.txt.open the file and write two lines.and add two lines.and read the lines.
f=open('Info.txt','w')
f.write('this is the first line')
f.write('\nthis is the second line')
f.close()
f=open('Info.txt','a')
f.write('\nthis is the third line')
f.write('\nthis is the fourth line')
f.close()
f=open('Info.txt','r') #replace
content = f.read()
f=open('Info.txt','w')
content =content.replace('this is the first line', 'we have made a change')
f.write(content)
print(content)
f.close()

# write a python that creates a text file named example. text,writes the following text into the file, and
#then reads and print the content of the file.
f=open('text.txt','w')
f.write('wel come to python')
f.write('\n we are working with python')
f.close()
f=open('text.txt','r')
res = f.readlines() #reading a oneline
print(res)


'''
'''
#17/3/25
import pandas as pd
data={
    'name':['Alice','bob','Charlie'],
    'Age':[24,27,28],
    'city':['new yark','los angles','chikago']
    
}
df=pd.DataFrame(data)
print(df)
df.to_csv('employees.csv',index=False)
df.to_json('employees.json',orient='records')
df_json=df
'''

import pandas as pd
data={
    'emp_id':[24,35,67],
    'emp_name':['Alice','Bob','John'],
    'emp_salary':[20000,25000,30000]
}
df=pd.DataFrame(data)
df.to_csv('employees1.csv',index=False)
df.to_json('employees1.json',orient='records')
'''

#to adding data to csv

import pandas as pd
data={
    'name':['Alice','bob','Charlie'],
    'Age':[24,27,28],
    'city':['new yark','los angles','chikago']
}

new_data=pd.DataFrame(data)
df_csv = pd.read_csv('employees.csv')
df_csv = pd.contact([df_csv, new_data],ignore_index=True)
df_csv.to_csv('employees.json',orient='records')


import pandas as pd
data={
    'name':['Alice','bob','Charlie'],
    'Age':[24,27,28],
    'city':['new yark','los angles','chikago']
}

new_data_json=pd.DataFrame(data)
df_json = pd.read_json('employees.csv')
df_json = pd.contact([df_json, new_data_json],ignore_index=True)
df_json.to_csv('employees.json',orient='records')
'''