from sys import stdin
input=stdin.readline

t=int(input().rstrip())
for _ in range(t):
    ps=input().rstrip()
    temp1=0
    temp2=0
    for i in ps:
        if temp1<temp2:
            break
        if i=='(':
            temp1+=1
        elif i==')':
            temp2+=1
    if temp1==temp2:
        print("YES")
    else:
        print("NO")