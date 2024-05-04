import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
five=0
three=0
if N%5==0:
    five=N//5
    N=0

while N>0:
    N-=3
    three+=1
    if N%5==0:
        five=N//5
        N=0
if N<0:
    print("-1")
else:
    print(f"{three+five}")