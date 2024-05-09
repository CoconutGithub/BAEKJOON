import sys
input=sys.stdin.readline
print=sys.stdout.write

N,M=map(int,input().rstrip().split())
str_n=[]
str_m=[]
for i in range(N):
    str_n.append(input().rstrip())
for i in range(M):
    str_m.append(input().rstrip())
cnt=0
str_n=set(str_n)
# dic={}
# for i in range(N):
#     dic[str_n[i]]=0
for i in str_m:
    if i in str_n:
        cnt+=1
print(f"{cnt}")