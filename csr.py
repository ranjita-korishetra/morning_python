
li=[]
print('enter the elements:')
for i in range(10):
    num=int(input())
    li.append(num)
print(li)


li=[1,2,3,4,5,6]
li.append((20,30))
print(li)

li =[3,4,5,6,7,8]
li.insert(0,20)
print(li)

li=[10,20,30]
li.pop(2)
print(li)

li=[10,20,30,40,50]
li.remove(20)
print(li)

li=[2,3,4,5,6]
pos=int(input('enter the position to be inserted:'))
num=int(input('enter the number to inserted:'))
li.insert(pos,num)
print(li)

ele=int(input('enter the number of deleted:'))
if ele in li:
    li.remove(ele)
print(li)

li=[10,20,40,90]
rem=int(input('enter the position to be deleted:'))
if rem in range(len(li)):
    li.pop(rem)
print(li)

li=[10,20,40,50,60]
num= int(input('enter the number of whose index has to be found:'))
if num in li:
    print(li.index(num))
else:
    print(-1)


tu=(1,2,3,4,5)
ele= int(input('enter the element whose index has to be determined:'))
if ele in tu:
    print('the index of',ele,'is',tu.index(ele))
else:
    print(ele,'is not present in the tuple')



s = set()
print('enter the elements:')
for i in range(5):
    num = int(input())
    s.add(num)
print(s)


s={1,2,3,4,5}
ele=int(input('enter the number of deleted:'))
if ele in s:
    s.remove(ele)
    print(s)
else:
    print(ele,'is not present int set')

se={10,20,40,90}
rem=int(input('enter the position to be deleted:'))
if rem in range(len(se)):
    se.pop(rem)
print(se)


user_info={}
user_info["name"] = input("Enter your name: ")
user_info["email"] = input("Enter your email: ")
user_info["mobile"] = input("Enter your mobile number: ")
user_info["city"] = input("Enter your city: ")
user_info["pin"] = input("Enter your PIN code: ")
print("\nUser Information:")
for key, value in user_info.items():
    print(f"{key}: {value}")

user_info={'name':'ranjita','email':'uiii','mobile':'9880','city':'fg','pin':'6546'}
new_name = input("\nEnter a new name : ")
user_info['name'] = new_name
for i,j in user_info.items():
    print(i,'=',j)
key_to_remove = input("Enter a key to remove from dictionary: ")
if key_to_remove in user_info:
    del user_info[key_to_remove]
    print(f"{key_to_remove} removed from dictionary.")
else:
    print(f"Key '{key_to_remove}' not found.")
value_to_check = input("Enter a value to check if it exists in the dictionary: ")
if value_to_check in user_info.values():
    print(f"The value '{value_to_check}' exists in the dictionary.")
else:
    print(f"The value '{value_to_check}' does not exist in the dictionary.")


x = list(range(0, 52, 2))
li=list(x)
print(li)


x = [10, 20, 30, 40, 50]
y = []

for i in range(5):
    if x[i] % 4 == 0:
        y.append(x[i])
print(y)

















