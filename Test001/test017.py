#2020.4.20 class
def myfuction (*args):
    print(args)
    for i in args:
        print(i)

myfuction(10,29,33)


def myfuction2(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My choice {}'.format(kwargs['fruit'])) #找出字典键对应的值
    else:
        print('no')

myfuction2(fruit='apple')
myfuction2(fruit='apple',veggie='lettcer')

print("*"*90)

def foo(required,*args,**kwargs):#至少需要一个requird参数
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)


foo('hello',1,2,3,key1='value')

print("*"*90)

def fib(n):
    a,b = 0,1
    while a<n:
        print(a,end=' ')
        a,b = b,a+b

def fib2(n):
    a,b=0,1
    for i in range(n):
        print(i,a)
        a,b=b,a+b

fib(18)
fib2(10)
print("*"*90)
def recursion():
    return recursion()

def fact(n):
    result=n
    for i in range(1,n):
        result=result*i
    return result
print(fact(6))

print("*"*90)

def fact1(n):
    if n==0:
        return 1
    return  n*fact1(n-1)
print(fact1(9))

#
def reverse(s):
    if s =='':
        return ''
    return reverse(s[1:])+s[0]
print(reverse('hello'))
print("*"*90)




