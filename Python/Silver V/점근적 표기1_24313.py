import sys
input=sys.stdin.readline
print=sys.stdout.write

a1,a0=map(int,input().rstrip().split())
c=int(input().rstrip())
n0=int(input().rstrip())
if(a1+a0/n0<=c and a1+a0/101<=c):
    print("1")
else:
    print("0")
