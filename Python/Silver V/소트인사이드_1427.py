import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
num=[]
while N>0:
    num.append(N%10)
    N//=10
num=sorted(num)[::-1]
for i in num:
    print(f"{i}")