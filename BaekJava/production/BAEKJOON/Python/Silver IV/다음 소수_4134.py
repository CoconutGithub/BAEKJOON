import sys
input=sys.stdin.readline
print=sys.stdout.write
import math

def is_prime(n):
    if n==1 or n==0:
        return False
    for i in range(2,int(math.sqrt(n))+1):#제곱근 구하기
        if n%i==0:
            return False
    return True
test=int(input().rstrip())
result=[]
num=[]

for i in range(test):
    num.append(int(input().rstrip()))
for i in num:
    temp=i
    while 1:
        if is_prime(temp):
            result.append(temp)
            break
        else:
            temp+=1
for i in result:
    print(f"{i}\n")

        