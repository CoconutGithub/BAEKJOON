import sys
input=sys.stdin.readline
print=sys.stdout.write

a,b=map(int,input().rstrip().split())
c,d=map(int,input().rstrip().split())

m=b*d
a*=d
c*=b
n=a+c
i=2
if n>m:
    while i<=m:
        if n%i==0 and m%i==0:
            n//=i
            m//=i
        else:
            i+=1
else:
    while i<=n:
        if n%i==0 and m%i==0:
            n//=i
            m//=i
        else:
            i+=1
print(f"{n} {m}")