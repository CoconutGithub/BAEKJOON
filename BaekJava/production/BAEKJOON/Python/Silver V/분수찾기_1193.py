import sys
input=sys.stdin.readline
print=sys.stdout.write

X=int(input().rstrip())
colum=0
a=0
b=0
#a/b

for i in range(1,100000000,1):
    colum+=i
    if(X<=colum):
        b=colum-X+1
        a=i+1-b
        break
    else:continue
if((a+b)%2==0):
    print(f"{b}/{a}\n")
else:print(f"{a}/{b}\n")