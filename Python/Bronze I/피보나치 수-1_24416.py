from sys import stdin
input=stdin.readline
l=[0]
def fib(n):
    if n==1 or n==2:
        l[0]+=1
        return 1
    else:
        return (fib(n-1)+fib(n-2))

def fibonacci(n):
    cnt=0
    f=['' for i in range(n)]
    f[0],f[1]=1,1
    for i in range(2,n):
        f[i]=f[i-1]+f[i-2]
        cnt+=1
    return cnt
n=int(input().rstrip())

fib(n)
print(f"{l[0]} {fibonacci(n)}")
