import sys
input=sys.stdin.readline
print=sys.stdout.write

N,K=map(int,input().rstrip().split())
num=[]
for i in range(1,N+1):
    if(N%i==0):
        num.append(i)
if(len(num)<K):
    print("0")
else:
    print(f"{num[K-1]}")