'''
x=int(input('enter the first number:'))
y=int(input('enter the second number:'))

if x>y:
    print(x,'is biggest among',y)
else:
    print(y,'is biggest among',x)
    '''
from xml.sax import make_parser

'''
a=int(input('enter the number:'))
if a%2==0:
    print(a,'is even number')
else:
    print(a,'is odd number')
    '''
'''
#vowel or consonants
ch=input('enetr the character:').lower()
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print(ch,'is a vowel')
else:
    print(ch,'is a consonent')
    '''
'''

year=int(input('enetr the year:'))
if  (year%400==0)or(year% 4==0 and year %100 !=0):
    print(year,' is a leap year')
else:
    print(year,'is not a leap year')
    '''
''''

a=input('Enter the string:')
if a==a[::-1]:
    print(a,'is a pallindrome')
else:
    print(a,'is not pallindrome')

    '''
'''

l=int(input('enter the length:'))
b=int(input('enter the bredth:'))
if l==b:
    print('it is square')
else:
    print('it is rectangle')

    '''
'''

gender=input('Enter the gender:')
height=int(input('Enter the height:'))
if gender.lower()=='male':
    if height>=188:
        print('eligible for admission')
    else:
        print('not eligible for admission')
elif gender.lower() =='female':
        if height >=175:
            print('eligible for admission')
        else:
            print('not eligible for admission')
'''
'''
num = int (input('enter the number:'))
if num%2==0:
    print(num,'is even')
else:
    print(num,'is odd')
    '''
'''
x=1
while x<=100:
    print(x)
    x=x+2
print('/n')
    '''
'''
x=2
while x<=100:
    print(x)
    x=x+2
print('/n')
    '''
'''
x=2
while x<=65536:
    print(x)
    x=x**2
print('end')
'''
'''
x=3125
while x>=5:
    print(x)
    x=x/5
print('end')
'''
'''
x=1
while x<=10:
    print(f'1*{x}={1*x}')
    x=x+1
    '''
'''

x=1
while x<=10:
    print(f'1*{x}={1*x},'
          f'2*{x}={2*x},'
          f'3*{x}={3*x},'
          f'4*{x}={4*x},'
          f'5*{x}={5*x},'
          f'6*{x}={6*x},'
          f'7*{x}={7*x},'
          f'8*{x}={9*x},'
          f'10*{x}={10*x}')
    x=x+1

'''
'''
let=['a','c','e','g','j']
i=0
while i<=4:
    print(let)
    i=i+1
    '''
'''
li = [10,20,30,40,50]
for i in li:
    print(i,end =' ')
'''
'''
li = [10,20,30,40,50]
for i in range(0,len(li),1):
    print(li[i],end =' ')
'''
'''
li = [10,20,13,61,50]
for i in range(len(li)-2,0,-2):
    print(li[i],end =' ')
'''
'''


li = [10,20,13,61,50]
print('elements at even indices are:')
for i in range(0,len(li),2):
    print(li[i], end=' ')
    print('\n')
print('elements at odd indices are:')
for i in range(1,len(li),2):
    print(li[i], end=' ')
    print('\n')
for i in li:
    if i%2==0:
        print(i,'is an even elements')
    else:
        print(i, 'is an odd elements')
print('\n')
sum = 0
for i in li:
    sum = sum + i
print('sum of even elements is',sum)
print('sum of odd elements is',sum)
'''
'''
li = [10,20,13,61,50]
print('sum of odd and even elements')
sum_even = 0
sum_odd =0
for i in li:
    if i % 2 == 0:
        sum_even= sum_even+i
    else:
        sum_odd = sum_odd + i
print('sum of even number is',sum_even)
print('sum of odd number is',sum_odd)
'''
'''
li = [10,20,13,61,50]
print('sum of odd and even indices')
sum_even = 0
sum_odd =0
for i in range(1,len(li),2):
        sum_even= sum_even+li[i]
for i in range(1,len(li),2):
        sum_odd = sum_odd + li[i]
print('sum of numbers at even indices is',sum_even)
print('sum of numbers at odd indices is',sum_odd)
'''



'''
li = [10, 20, 13, 61, 50]
for i in range(len(li) - 2, 0, -2):
    print(li[i], end=' ')
'''
'''

li = [10, 20, 30, 40, 50]
for i in range(0, len(li),3):
    print(li[i], end=' ')
       '''
'''
x = input('enter a string:')
word_count = 0
space_count = 0
for char in x:
    if char ==' ':
        space_count +=1
word_count +=1
print('number of words:',word_count)
print('number of space:',space_count)


char = input('enter the character:')
vowels = ['a','e','i','o','u']
for char in vowels:
    print(f'{char} is a vowel')
else:
    print(f'{char} is not a vowel')
'''
'''
li = [10,200,30,400,50]
biggest = 0
for item in li:
    if item > biggest:
        biggest=item
print(biggest)
'''
li = [10,2,6,4,5]
smallest =li[0]
for i in range(len(li)):
    if li[i] < smallest:
        smallest=li[i]
print(smallest)















