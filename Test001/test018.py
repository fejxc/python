def findfib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return findfib(n-1)+findfib(n-2)
def main():
    x=int(input())
    print(findfib(x)%10007)
if __name__ == '__main__':
    main()

"""def printfib(n):
    a,b=1,2
    for i in range(1,n):
        print("{0}个fib数是：{1}".format(i,a))
        a,b=b,a+b
print(printfib(10))"""
