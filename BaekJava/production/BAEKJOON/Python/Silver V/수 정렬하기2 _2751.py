import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
num=[]
for i in range(N):
    num.append(int(input().rstrip()))
num=sorted(num)
for i in num:
    print(f"{i}\n")