import sys
input=sys.stdin.readline
print=sys.stdout.write

A,B=map(int,input().rstrip().split())
a=set(input().rstrip().split())
b=set(input().rstrip().split())

print(f"{len(a-b)+len(b-a)}")