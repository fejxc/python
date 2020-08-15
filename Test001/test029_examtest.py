#迭代器
from _collections_abc import Iterable

print(isinstance([1,2,3],Iterable))
x=iter([1,2,3,4,5])

print(next(x))
print(next(x))
for i in x:
    print(i,end='-->')


#生成器
def scq():
    yield 1
    yield 2
    yield 3
    yield "sunyun"

st=scq()
print(next(st))

a=(i*2 for i in range(0,3)) #生成器表达式用（ ） -----  列表表达式用[ ]
print(a)
print(next(a))