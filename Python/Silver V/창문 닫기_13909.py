from sys import stdin,stdout
input=stdin.readline
print=stdout.write

n=int(input().rstrip())
cnt=1
#창문이 1로 열려있으려면 소수가 홀수개 있어야함
#->제곱수와 1만 열림
for i in range(2,n+1):
    if i**2<=n:
        cnt+=1
print(f"{cnt}")

#범위가 2100000000까지라 전부 다 넣으면 메로리 초과
# window={}
# for i in range(1,n+1):
#     window[i]=1

# for i in range(2,n+1):
#     for j in range(1,n//i+1):
#         window[i*j]=complement(window[i*j])

# cnt=0
# for i in range(1,n+1):
#     if window[i]==1:
#         cnt+=1

# print(f"{cnt}")
