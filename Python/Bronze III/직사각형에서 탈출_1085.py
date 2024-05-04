import sys
input=sys.stdin.readline
print=sys.stdout.write

x,y,w,h=map(int,input().rstrip().split())
point=[x,y,w-x,h-y]
print(f"{min(point)}")