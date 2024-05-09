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

T=int(input().rstrip())
result=[]
#prime을 set형식으로 생성 후 소수만 담음
#(for문 안 is_prime 밖으로 뺌)
prime=set()
for i in range(1000001):
    if is_prime(i):
        prime.add(i)
for i in range(T):
    n=int(input().rstrip())
    cnt=0
    for j in range(2,n//2+1):
        if j in prime and (n-j) in prime:
            cnt+=1
    result.append(cnt)
for i in result:
    print(f"{i}\n")

#시간 초과
# for i in range(T):
#     n=int(input().rstrip())
#     cnt=0
#     for j in range(2,n//2+1):
#         if is_prime(j) and is_prime(n-j):
#             cnt+=1
#     result.append(cnt)
# for i in result:
#     print(f"{i}\n")