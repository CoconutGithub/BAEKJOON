import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
point=[]
for i in range(N):
    temp=list(map(int,input().rstrip().split()))
    point.append(temp)
point=sorted(point)
for i in range(N):
    print(f"{point[i][0]} {point[i][1]}\n")

#     x.append(temp_x)
#     y.append(temp_y)
# for i in range(N):
#     for j in range(1,N):
#         if x[j]<x[j-1]:
#             x[j],x[j-1]=x[j-1],x[j]
#             y[j],y[j-1]=y[j-1],y[j]
# for i in range(1,N):
#     if x[i]==x[i-1] and y[i]<y[i-1]:
#         y[i],y[i-1]=y[i-1],y[i]
# for i in range(N):
#     print(f"{x[i]} {y[i]}\n")
#시간초과
