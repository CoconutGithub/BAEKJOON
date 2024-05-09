import sys
input=sys.stdin.readline
print=sys.stdout.write

island=int(input().rstrip())
price=list(map(int,input().rstrip().split()))
print(f"{sum(price)-max(price)}")
