import sys
input=sys.stdin.readline
print=sys.stdout.write

N,M=map(int,input().rstrip().split())
result=[i+1 for i in range(N)]
for i in range(M):
    a,b=map(int,input().rstrip().split())
    result[a-1],result[b-1]=result[b-1],result[a-1]
    # temp=result[a-1]
    # result[a-1]=result[b-1]
    # result[b-1]=temp
for i in result:
    print(f"{i} ")
