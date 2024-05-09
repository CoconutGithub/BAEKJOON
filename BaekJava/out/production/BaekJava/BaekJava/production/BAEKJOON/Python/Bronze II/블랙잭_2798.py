import sys
input=sys.stdin.readline
print=sys.stdout.write

N,M=map(int,input().rstrip().split())
card=list(map(int,input().rstrip().split()))
three=[]
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            three.append(card[i]+card[j]+card[k])
three=sorted(list(set(three)))
for i in three:
    if i<=M:
        temp=three.index(i)
    elif i>M:
        temp=three.index(i)-1
        break
print(f"{three[temp]}")
