from sys import stdin
input=stdin.readline
from collections import deque

n=int(input().rstrip())
card=deque([i for i in range(1,n+1)])

i=0
while 1:
    if len(card)==1:
        break
    if i%2==0:
        card.popleft()
        i+=1
    else:
        card.append(card.popleft())
        i+=1
print(f"{card[0]}")