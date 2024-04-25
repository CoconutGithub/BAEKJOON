import sys
input=sys.stdin.readline
print=sys.stdout.write

n=int(input().rstrip())
num=[]
all=0
for i in range(1,n-1):
    all+=i
    num.append(all)
print(f"{sum(num)}\n3")
