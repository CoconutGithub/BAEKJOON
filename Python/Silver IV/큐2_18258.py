from sys import stdin
input=stdin.readline

n=int(input().rstrip())
queue=[]

for i in range(n):
    order=input().rstrip().split()
    if order[0]=='push':
        queue.append(order[1])
    elif order[0]=='pop':
        if len(queue)>0:
            print(f"{queue.pop(0)}")
        else:
            print("-1")
    elif order[0]=='size':
        print(f"{len(queue)}")
    elif order[0]=='empty':
        if len(queue)==0:
            print("1")
        else:
            print("0")
    elif order[0]=='front':
        if len(queue)>0:
            print(f"{queue[0]}")
        else:
            print("-1")
    elif order[0]=='back':
        if len(queue)>0:
            print(f"{queue[-1]}")
        else:
            print("-1")