import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
num=[]
for i in range(N):
    num.append(int(input().rstrip()))

for j in range(N):
    for i in range(1,N):
        if num[i-1]>num[i]:
            num[i-1],num[i]=num[i],num[i-1]
for i in num:
    print(f"{i}\n")

