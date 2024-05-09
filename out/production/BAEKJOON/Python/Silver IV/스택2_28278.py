from sys import stdin
input=stdin.readline

n=int(input().rstrip())
stack=[]
for i in range(n):
    order=list(map(int,input().rstrip().split()))
    if order[0]==1:
        stack.append(order[1])
    elif order[0]==2:
        if len(stack)==0:
            print("-1")
        elif len(stack)!=0:
            print(f"{stack.pop()}")
    elif order[0]==3:
        print(f"{len(stack)}")
    elif order[0]==4:
        if len(stack)==0:
            print("1")
        else:
            print("0")
    elif order[0]==5:
        if len(stack)==0:
            print("-1")
        elif len(stack)!=0:
            print(f"{stack[-1]}")
