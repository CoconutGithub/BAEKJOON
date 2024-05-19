from sys import stdin
input=stdin.readline
#재귀로 풀어야되는 문제
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)

n=int(input().rstrip())
print(fib(n))
