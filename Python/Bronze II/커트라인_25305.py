import sys
input=sys.stdin.readline
print=sys.stdout.write

N,k=map(int,input().rstrip().split())
score=list(map(int,input().rstrip().split()))
cut=[]
for i in range(k):
    cut.append(max(score))
    score.remove(max(score))
print(f"{min(cut)}")
