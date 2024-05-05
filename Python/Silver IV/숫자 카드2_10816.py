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

for i in card_m:
    print(f"{dic[i]} ")

#card_m에 중복이 있을 수 있음(문제에 설명이 없어서 힘들었다)
#딕셔너리에는 중복이 불가능하므로 틀렸다고 나왔다
# for i in dic.values():
#     print(f"{i} ")