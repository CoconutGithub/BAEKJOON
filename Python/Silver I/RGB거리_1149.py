from sys import stdin
input=stdin.readline

n=int(input().rstrip())
dp=['' for i in range(n)]

for i in range(n):
    dp[i]=list(map(int,input().rstrip().split()))

r,g,b=['' for i in range(n)],['' for i in range(n)],['' for i in range(n)]
r[0],g[0],b[0]=dp[0][0],dp[0][1],dp[0][2]
for i in range(1,n):
    r[i]=min(g[i-1],b[i-1])+dp[i][0]
    g[i]=min(r[i-1],b[i-1])+dp[i][1]
    b[i]=min(g[i-1],r[i-1])+dp[i][2]
    print(f"**{r[i],g[i],b[i]}")
print(min(r[n-1],g[n-1],b[n-1]))



# sum=min(dp[0])
# for i in range(1,n):
#     dp[i][dp[i-1].index(min(dp[i-1]))]=1001
    
#     sum+=min(dp[i])
# print(dp)
# print(sum)
