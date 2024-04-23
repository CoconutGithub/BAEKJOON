import sys
input=sys.stdin.readline
print=sys.stdout.write

A,B,V=map(int,input().rstrip().split())
day=(V-B)/(A-B)
if day%1>0:
    day+=1
    print(f"{int(day)}")
else:
    print(f"{int(day)}")
