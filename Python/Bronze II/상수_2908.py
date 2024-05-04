import sys
input=sys.stdin.readline
print=sys.stdout.write

A,B=map(str,input().rstrip().split())
A=int(A[::-1])
B=int(B[::-1])
if(A>B):
    print(f"{A}")
else:
    print(f"{B}")