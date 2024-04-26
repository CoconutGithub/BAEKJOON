import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
result=0
for i in range(1000000):
    num=[]
    temp=i
    num.append(i)
    while i>0:
        num.append(i%10)
        i//=10
    if sum(num)==N:
        result=temp
        break
print(f"{result}")