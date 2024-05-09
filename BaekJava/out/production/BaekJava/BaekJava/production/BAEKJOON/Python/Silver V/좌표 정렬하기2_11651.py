import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
point=[]
for i in range(N):
    temp=list(map(int,input().rstrip().split()))[::-1]
    point.append(temp)
point=sorted(point)
for i in range(N):
    print(f"{point[i][1]} {point[i][0]}\n")


