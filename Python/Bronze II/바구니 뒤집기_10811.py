import sys
input=sys.stdin.readline
print=sys.stdout.write

N,M=map(int,input().rstrip().split())
basket=[i+1 for i in range(N)]
for t in range(M):
    i,j=map(int,input().rstrip().split())
    temp=basket[i-1:j]
    temp=temp[::-1]
    # for r in temp:
    #     basket[i-1]=r
    #     i+=1
    basket[i-1:j]=temp
for i in basket:
    print(f"{i} ")