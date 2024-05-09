import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
count=0
num=list(map(int,input().rstrip().split()))
try:
    num.remove(1)
except ValueError:
    pass
for j in num:
    factor=[]
    for k in range(2,j):
        if j%k==0:
            factor.append(k)
    if len(factor)==0:
        count+=1
print(f"{count}")