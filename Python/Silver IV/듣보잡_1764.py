import sys
input=sys.stdin.readline
print=sys.stdout.write

N,M=map(int,input().rstrip().split())
name_n,name_m=set(),set()
for i in range(N):
    name_n.add(input().rstrip())
for i in range(M):
    name_m.add(input().rstrip())
name=[]
cnt=0
for i in name_m:
    if i in name_n:
        name.append(i)
        cnt+=1
print(f"{cnt}\n")
name.sort()
for i in name:
    print(f"{i}\n")
