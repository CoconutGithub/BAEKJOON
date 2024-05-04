import sys
input=sys.stdin.readline
print=sys.stdout.write

test=int(input().rstrip())
graph=[[0 for i in range(100)]for j in range(100)]

for i in range(test):
    x,y=map(int,input().rstrip().split())
    for a in range(x,x+10):
        for b in range(y,y+10):
            graph[a][b]=1
sum=0
for i in range(100):
    sum+=graph[i].count(1)
print(f"{sum}")
