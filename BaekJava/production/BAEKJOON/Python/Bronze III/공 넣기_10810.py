import sys
input=sys.stdin.readline
print=sys.stdout.write

N,M=map(int,input().rstrip().split())
result=[0 for i in range(N)]
for i in range(M):
    a,b,c=map(int,input().rstrip().split())
    for j in range(a-1,b):
        result[j]=c
for i in result:
    print(f"{i} ")
