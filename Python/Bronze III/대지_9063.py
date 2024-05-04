import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
x,y=[],[]
for i in range(N):
    temp=list(map(int,input().rstrip().split()))
    x.append(temp[0])
    y.append(temp[1])

print(f"{(max(x)-min(x))*(max(y)-min(y))}")