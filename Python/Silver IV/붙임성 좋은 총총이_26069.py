from sys import stdin
input=stdin.readline

n=int(input().rstrip())
dance={'ChongChong':1}
for _ in range(n):
    temp=input().rstrip().split()
    if temp[0] not in dance:
        dance[temp[0]]=0
    if temp[1] not in dance:
        dance[temp[1]]=0
    if dance[temp[0]] or dance[temp[1]]:
        dance[temp[1]]=1
        dance[temp[0]]=1

cnt=0
for i in dance.values():
    if i==1:
        cnt+=1
print(cnt)