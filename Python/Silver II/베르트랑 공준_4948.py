import sys
input=sys.stdin.readline
print=sys.stdout.write
from math import sqrt

def is_prime(n):
    if n==1 or n==0:
        return False
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            return False
    return True

result=[]
while 1:
    cnt=0
    n=int(input().rstrip())
    if n==0:
        break
    for i in range(n+1,2*n+1):
        if is_prime(i):
            cnt+=1
    result.append(cnt)

for i in result:
    print(f"{i}\n")