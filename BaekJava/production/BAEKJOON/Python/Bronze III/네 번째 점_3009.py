import sys
input=sys.stdin.readline
print=sys.stdout.write

x=[]
y=[]
result=""
for i in range(3):
    temp=list(map(int,input().rstrip().split()))
    x.append(temp[0])
    y.append(temp[1])
for i in x:
    if x.count(i)==1:
        result+=f"{i} "
for i in y:
    if y.count(i)==1:
        result+=f"{i}"
print(f"{result}")