from sys import stdin
input=stdin.readline
from collections import deque

n=int(input().rstrip())
a=list(map(int,input().rstrip().split()))
cnt=a.count(0)
b=list(map(int,input().rstrip().split()))
que=deque()
for i in range(n):
    if a[i]==0:
        que.appendleft(b[i])
m=int(input().rstrip())
c=list(map(int,input().rstrip().split()))
if cnt<=m:
    for i in c:
        que.append(i)
    for i in range(m):
        print(que.popleft(),end=" ")
else:
    for i in range(m):
        print(que.popleft(),end=" ")



