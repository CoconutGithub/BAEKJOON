import sys
input=sys.stdin.readline
print=sys.stdout.write

a=1
b=1
while 1:
    a,b=map(int,input().rstrip().split())
    if(a==0 and b==0):
        break
    else:
        print(f"{a+b}\n")