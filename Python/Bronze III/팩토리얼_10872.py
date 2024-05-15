from sys import stdin
input=stdin.readline

n=int(input().rstrip())
fac=1
for i in range(1,n+1):
    fac*=i
print(fac)