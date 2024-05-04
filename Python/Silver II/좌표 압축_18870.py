import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
# point=list(map(int,input().rstrip().split()))
# num=[]
# for i in point:
#     cnt=0
#     dup=0
#     for j in point:
#         if i>j and point.count(j)>1:
#             dup+=1
#             cnt+=1
#         elif i>j:
#             cnt+=1
#     if dup>1:
#         num.append(cnt-(dup-1))
#     else:
#         num.append(cnt)
# print(f"{num}")
## 시간 초과

point=list(map(int,input().rstrip().split()))
temp=sorted(set(point))
dic={}
for i in range(len(temp)):
    dic[temp[i]]=i
result=[]
for i in range(N):
    result.append(dic[point[i]])
for i in result:
    print(f"{i} ")
#딕셔너리는 신이야!!!!!!!

