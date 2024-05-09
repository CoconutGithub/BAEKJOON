import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
card_n=list(map(int,input().rstrip().split()))
M=int(input().rstrip())
card_m=list(map(int,input().rstrip().split()))
dic={}
result=[]
for i in range(N):
    dic[card_n[i]]=0
for i in card_m:
    if i in dic:#딕셔너리에서 찾는거는 O(1)이라고함
        result.append(1)
    else:
        result.append(0)
for i in result:
    print(f"{i} ")
