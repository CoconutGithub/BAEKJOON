from sys import stdin
input=stdin.readline
from collections import deque

n=int(input().rstrip())
deq=deque()
for i in range(n):
    order=input().rstrip().split()
    if int(order[0])==1:
        deq.appendleft(order[1])
    elif int(order[0])==2:
        deq.append(order[1])
    elif int(order[0])==3:
        if len(deq)>0:
            print(deq.popleft())
        else:
            print(-1)
    elif int(order[0])==4:
        if len(deq)>0:
            print(deq.pop())
        else:
            print(-1)
    elif int(order[0])==5:
        print(len(deq))
    elif int(order[0])==6:
        if len(deq)>0:
            print(0)
        else:
            print(1)
    elif int(order[0])==7:
        if len(deq)>0:
            print(deq[0])
        else:
            print(-1)
    elif int(order[0])==8:
        if len(deq)>0:
            print(deq[-1])
        else:
            print(-1)

