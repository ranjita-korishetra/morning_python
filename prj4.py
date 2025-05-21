'''
house_number=int(input('enter the house number:'))
street=(input('enter the street:'))
city=(input('enter the city:'))
pincode=int(input('enter the pincode:'))
di = {
    'house number':house_number,
    'street':street,
    'city':city,
    'pincode':pincode
}

for i,j in di.items():
    print(i,j)
'''
'''

li = []
for i in range(5):
    num = int(input('enetr the number:'))
    li.append(num)
print(li)
'''
num = int(input('enter the number:'))
res = num
rev = 0
while num>0:
    rem = num%10
    rev = (rev*10)+rem
    num = num//10
if rev == res:
    print(res,'is a palindrome number')
else:
    print(res,'is not a palindrome number')





