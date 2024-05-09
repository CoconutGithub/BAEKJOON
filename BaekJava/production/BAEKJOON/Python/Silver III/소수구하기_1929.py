import sys
input=sys.stdin.readline
print=sys.stdout.write
import math

M,N=map(int,input().rstrip().split())
result=[]

def is_prime(n):
    if n==1 or n==0:
        return False

    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

for i in range(M,N+1):
    if is_prime(i):
        result.append(i)

for i in result:
    print(f"{i}\n")
