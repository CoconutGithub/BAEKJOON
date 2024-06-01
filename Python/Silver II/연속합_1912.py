from sys import stdin
input=stdin.readline

n=int(input().rstrip())
l=list(map(int,input().rstrip().split()))

dp=[-2000 for _ in range(n+1)]#처음에 나올 수 있는 가장 작은 수인 -2000주고 더해가면서 큰거 가져감
for i in range(1,n+1):
    dp[i]=max(l[i-1],dp[i-1]+l[i-1])#처음부터 하나씩 더해가면서 연속된 숫자로 더했을 때 큰걸 가져감

print(max(dp))

#시간초과 너무 커짐
# m=-2000
# for i in range(n):
#     for j in range(n-i):
#         if sum(l[j:j+i+1])>m:
#             m=sum(l[j:j+i+1])
# print(m)