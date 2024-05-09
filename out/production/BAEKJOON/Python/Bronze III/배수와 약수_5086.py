import sys
input=sys.stdin.readline
print=sys.stdout.write

a=1
b=1
while a!=0 and b!=0:
    a,b=map(int,input().rstrip().split())
    if(a==0 or b==0):
        break
    if(a%b==0):
        print("multiple\n")
    elif(b%a==0):
        print("factor\n")
    else:
        print("neither\n")