import sys
input=sys.stdin.readline
print=sys.stdout.write

M=int(input().rstrip())
N=int(input().rstrip())

num=[]
for i in range(M,N+1):
    factor=[]
    for j in range(1,i):
        if i%j==0:
            factor.append(j)
    if len(factor)-1==0:
        num.append(i)

if len(num)==0:
    print("-1")
else:
    print(f"{sum(num)}\n")
    print(f"{min(num)}")

            