import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
num=[0 for i in range(10000)]
for i in range(N):
    temp=int(input().rstrip())
    num[temp-1]+=1

for i in range(10000):
    if num[i]>0:
        for j in range(num[i]):
            print(f"{i+1}\n")


