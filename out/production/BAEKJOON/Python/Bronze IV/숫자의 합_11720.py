import sys
input=sys.stdin.readline
print=sys.stdout.write

num=int(input().rstrip())
string=input().rstrip()
sum=0
for i in string:
    sum+=int(i)
print(f"{sum}")
    