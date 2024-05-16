from sys import stdin
input=stdin.readline

n=int(input().rstrip())
fac=list(map(int,input().rstrip().split()))
print(min(fac)*max(fac))