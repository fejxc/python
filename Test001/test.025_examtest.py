a={'one':1,'two':2,'three':3}

for k,v in a.items():
    print(k,v,end='\n')

quetions=['name','quest','favorite cocol']
answers=['Sunyun','To seek the holy gray','Red']

for i,j in zip(quetions,answers):
    print('What is your{0}?  {1}.'.format(i,j))
b=list()
for i in reversed(range(1,11,2)):
    print(i,end="->")
    b.append(i)
print('\n'+'*'*40)
print(sorted(b))
a=[346,76,546,1,6,2]
print(sorted(a))
print('\n'+'*'*40)
print("列表推导表达式")
res1=[(x,x**2,x**3)for x in range(5)]
print(res1)
# res2=[(i,j)for i in range(5) for j in range(i)]
# print(res2)
res3=[(x*2+1)for x in range(4) ]
print(res3)
res4=[(x%3==0) for x in [3,5,9,8]]
print(res4)
res5=[(x*x) for x in range(10)]
print(res5)
res6=[(x[0].upper()) for x in ['apple','organg','pear'] ]
print(res6)
res7=[(x) for x in ['apple','organg','pear'] if len(x)<=5]
print(res7)
res8=[(x,len(x)) for x  in ['apple','organg','pear']]
print(res8)
print('\n'+'*'*40)
print("函数进阶")
#求阶乘
def factor(n):
    if n==1:
        return 1
    else:
        return n*factor(n-1)
print(factor(5))
#求x的n次幂
def power(x,n):
    if n==0:
        return 1
    else:
        return power(x,n-1) * x
print(power(2,10))
#求fib数列
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return  fib(n-2)+fib(n-1)
print(fib(5))
for i in range(1,11):
    print(fib(i),end=",")