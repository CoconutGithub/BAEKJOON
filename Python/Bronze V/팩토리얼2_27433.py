from sys import stdin
input=stdin.readline
#팩토리얼2는 재귀를 사용해서 푸는 문제
def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

print(factorial(int(input().rstrip())))