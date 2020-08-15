# print(0.1 + 0.2 == 0.3)  #False
#
# print(0.2 + 0.2 == 0.4)  #True

#看浮点运算--->>为什么 第一个是False  stackoverflow

# print(0.1+0.2)  #0.30000000000000004
# print(0.3-0.1)  #0.19999999999999998
#
# from numpy import *
# import numpy as np
# a=eye(4)
# print(a)
# print(ndim(a))
# print(a[:,1])
# b=np.array([3,4,5])
# c=b+4
# print(c)

# class A():
#     def a(self):
#         print('a')
# class B():
#     def b(self):
#         print('b')
# class C():
#     def c(self):
#         print('c')
# class D(A,B,C):
#     def d(self):
#         print("d")
# d=D()
# d.a()
# d.b()
# d.d()
rt1=map(lambda x:sum(x),[[1,3],[4,2,-5]])
print(list(rt1))
rt2=':'.join(list(map(str,[1,True,[2,3]])))
print(rt2)
rt3=filter(lambda x:x!=0 and x!='A',[0,1,0,6,'A',1,0,7])
print(list(rt3))