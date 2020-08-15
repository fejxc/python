data = [-1, 2, 3, -4, 5]
re=[]
for x in data:
    if x>0:
        re.append(x)
print(re)
re_2=[x for x in data if x>0]
print(re_2)

re_3=[i for i in data if i<0]
print(re_3)

from random import randint
d={'student%d'% i:randint(50,100) for i in range(1,20)}
print(d)

d1={k:v for k,v in d.items() if v>=90}
print(d1)
a={'sun':99,'yu':90,'tu':80,'xu':100}
a1={k:v for k,v in a.items() if v>=95}
print(a1)

print("*"*60)

s={randint(0,20) for i in range(20)}
print(s)
s1={x for x in s if x%2!=0}
print(s1)
print("*"*60)

d = {k: randint(60, 100) for k in 'abcdefg'}
print(d)
list1=[(v,k) for v,k in d.items()]
print(list1)
list1=sorted(list1,reverse=True)
list2=sorted(list1)
print(list1)
print(list2)
print("*"*60)
print()
#zip函数
a=['phone_mobile','phone_mobile price','phone_mobile_color']
b=['Appele','5699','white']
for i , j in zip(a,b):
    print('What is your{0}? {1}.'.format(i,j))
print("*"*70)
for i in sorted(b):
    print(i)
print("*"*70)
for i in reversed(b):
    print(i)
print("*"*70)
for i in b:
    print(i)
print("*"*70)

s=[]
for i in range(100):
    s.append(i+1)
print(s[:5]+s[-5:])
furit=['apple','orange','banana','pear']
result=[(x,len(x)) for x in furit ]
print(result)
result2=[x for x in furit if len(x)<=5]
print(result2)
result3=[x[0:1].upper() for x in furit]
print(result3)