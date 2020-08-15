"""
lambda函数

seq = ["foo", "x41", "!!", "***"]
def func(x):
    return x.isalnum()

list(filter(func, seq))

lambda x: True if x.isalnum() else False
list(filter(lambda x:x.isalnum(),seq))
"""
newlist = filter(lambda x: x % 3 == 0, [1, 2, 3])
print(list(newlist))

print("--"*30)

def f1():
    return (lambda :3)()
f1()

def f2():
    return (lambda :lambda :3)()
f2()()

def f3():
    return (lambda :lambda x:3)()
f3()(3)

def f4():
    return (lambda :lambda :lambda x:lambda :3)()
f4()
