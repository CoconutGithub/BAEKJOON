import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
card_n=list(map(int,input().rstrip().split()))
M=int(input().rstrip())
card_m=list(map(int,input().rstrip().split()))
dic={}
for i in range(M):
    dic[card_m[i]]=0
for i in card_n:
    if i in dic:
        dic[i]+=1
for i in dic.values():
    print(f"{i} ")