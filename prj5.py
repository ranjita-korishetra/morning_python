'''
def function(x,y):
    print(x+y)
function(10,20)
'''
'''
def function(x,y):
    print('x=',x)
    print('y=',y)
function(10,20)
'''
'''
def function(x,y):
    print('x=',x)
    print('y=',y)
function(y=10, x=20)
'''
'''
def function(name,mobile,course='python'):
    print(name,mobile,course)
function('ranju',234,'java')
'''
def function(*a):
    print(a)
function()
function(1)
function(1,2,3)
function(1,'ranju','java',9.8,1000)

'''
def fun(pname,b_group,*disease,email='nothing'):
    print('pname=',pname)
    print('bgroup=',b_group)
    for i in disease:
    print(i,end=' ')
    print('/n')
    print('email=',email)
fun('ranjita','a+','cold','fever',)
'''
def fun(sname,*email,**address):
    print(sname)
    for i in email:
        print(i)
    print('\n' )
    for j in address:
        print(j,end=' ')
fun('sneha','shombali','hirekerur','bangalore')


