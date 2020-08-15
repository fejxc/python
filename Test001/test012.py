def fib(n):
    a,b=1,2;
    for i in range(n):
        #print('第一个{0}个fib数:{1}'.format(i,a))
        print(a,end=' ')
        a,b=b,a+b
fib(20)
print()
print("*"*80)
def add(x,y):
    result=x+y
    return result

x=add(1,3)
print(x)
def muti(x,y):

    result=x*y
    return result


print(muti(6,1))
print("*"*80)
print()
def isPass(s0,s1):
    s0=int(s0)
    s1=int(s1)
    if(s0)>=75:
        if(s1>=75):
           # print("通过")
            return 0
        else:
            #print("面试不通过")
            return 1
    else:
        if(s1)>80:
            #print('笔试不通过')
            return 2
        else:
            #print("笔试面试都不通过")
            return 3

people=[('孙昀',80,89),('涂慧',70,89),('程华飞',80,77),('嘿嘿',77,77),('花花',80,99)]
passall=[]
for i in range(0,len(people)):
    name=people[i][0]
    s0=people[i][1]
    s1=people[i][2]
    x=isPass(s0,s1)
    if(x==0):
        print(name+"通过")
        passall.append(name)
    if(x==1):
        print(name+"面试不通过")
    if(x==2):
        print(name+'笔试不通过')
    if(x==3):
        print(name+"笔试面试都不通过")
print("面试通过的所有名单：")
print(passall)
