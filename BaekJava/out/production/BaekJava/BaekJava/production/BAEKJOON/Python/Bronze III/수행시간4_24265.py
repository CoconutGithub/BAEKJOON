import sys
input=sys.stdin.readline
print=sys.stdout.write
n=int(input().rstrip())
sum=0
for i in range(1,n):
    sum+=i
print(f"{sum}\n2")