import sys
input=sys.stdin.readline
print=sys.stdout.write

N,M=map(int,input().rstrip().split())
A=[[0 for i in range(M)]for j in range(N)]
B=[[0 for i in range(M)]for j in range(N)]
for i in range(N):
    temp=list(map(int,input().rstrip().split()))
    for j in range(M):
        A[i][j]=temp[j]
for i in range(N):
    temp=list(map(int,input().rstrip().split()))
    for j in range(M):
        B[i][j]=temp[j]
for i in range(N):
    for j in range(M):
        print(f"{A[i][j]+B[i][j]} ")
    print('\n')