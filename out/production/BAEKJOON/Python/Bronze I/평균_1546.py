import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
subject=list(map(int,input().rstrip().split()))
average=0
for i in subject:
    average+=i/max(subject)*100
print(f"{average/N}")