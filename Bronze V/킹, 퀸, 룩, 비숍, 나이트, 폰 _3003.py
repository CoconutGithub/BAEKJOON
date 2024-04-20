import sys
input=sys.stdin.readline
print=sys.stdout.write

chess=list(map(int,input().rstrip().split()))
origin=[1,1,2,2,2,8]
for i in range(6):
    print(f"{origin[i]-chess[i]} ")