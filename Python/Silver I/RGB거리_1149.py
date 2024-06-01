from sys import stdin
input=stdin.readline

n=int(input().rstrip())
dp=['' for i in range(n)]

for i in range(n):
    dp[i]=list(map(int,input().rstrip().split()))#각 집마다 칠하는 비용 저장

r,g,b=['' for i in range(n)],['' for i in range(n)],['' for i in range(n)]#마지막으로 칠한게 r,g,b인 값을 저장하는 배열
r[0],g[0],b[0]=dp[0][0],dp[0][1],dp[0][2]#일단 초기값 설정
for i in range(1,n):
    r[i]=min(g[i-1],b[i-1])+dp[i][0]#i번째 집에 빨강으로 칠하는 경우 중에 i-1번째 집을 g,b로 칠한 것중 작은 것 + 이번 집을 r로 칠하는 값
    g[i]=min(r[i-1],b[i-1])+dp[i][1]
    b[i]=min(g[i-1],r[i-1])+dp[i][2]
print(min(r[n-1],g[n-1],b[n-1]))
