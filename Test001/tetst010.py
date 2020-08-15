'''
for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={j*i}',end=' ')
    print()
'''

s1='(555) 555-5555'

x=[i for i in s1 if i.isdigit()]
s2=''.join(x)

print(s2)
print(len(s2))
if s2.isdigit() and len(s2)>=10:
    print(s2[0:3]+'.'+s2[3:6]+'.'+s2[6:])


    print(s2)

else:
    print('Please enter a 10-digit phone number.')

