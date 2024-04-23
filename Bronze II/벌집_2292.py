import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
num=1
count=1
while num<N:
    num+=6*count
    count+=1
print(f"{count}")