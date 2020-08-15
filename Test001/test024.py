print('1024的二进制：'+bin(1024)) #转换2进制
print('1024的16进制：'+hex(1024)) #转换16进制
print(oct(1024))

x = 5.23222
print("%.2f" %x)
print(round( x , 2 ))

s='hello ahoa jjad, Aoedk ?'
print(s.islower())

s2 = 'wwwhsjhhwjwwwwwwww'
print(s2.count('w'))

set1 ={2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))
print(set1-set2)
print(set([y for y in set1 if y not in set2]))

#找出在任一集合中的元素 set1 set2 集合

print(set1.union(set2))

print([x*3 for x in range(10)])

print({x:x**3 for x in range(5)})

I = [5,1,2,3,4]
reversed(I)
print(list(reversed(I)))
print(I.reverse())

I.sort()
print(I.sort())


print(sorted(I))

#类class另一个名称是什么  kind type