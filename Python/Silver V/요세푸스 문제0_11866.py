from sys import stdin
input=stdin.readline
from collections import deque

n,k=map(int,input().rstrip().split())
josephus=deque([i for i in range(1,n+1)])
result=[]
while len(josephus)!=0:
    josephus.rotate(-(k-1))
    result.append(josephus.popleft())
p=[]
p.append("<")
for i in result:
    p.append(i)
    p.append(", ")
p.pop()
p.append(">")
for i in p:
    print(i,end="")