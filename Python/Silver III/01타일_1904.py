from sys import stdin
input=stdin.readline

n=int(input().rstrip())

l=[''for i in range(n+1)]
l[0]=1
l[1]=2
for i in range(2,n):
    l[i]=(l[i-1]+l[i-2])%15746

print(l[n-1])

#아래처럼 짜면서 피보나치라는걸 깨달음
#일단 그냥 재귀로 짜보니 숫자가 커지면서 재귀 오류 발생
# dic=dict()
# def tile(n):
#     if n==2:
#         return 2
#     elif n==1:
#         return 1
#     elif n==0:
#         return 0
    
#     if n in dic:
#         return dic[n]
    
#     if n>1:
#         dic[n]=(tile(n-1)+tile(n-2))%15746
#         return dic[n]
