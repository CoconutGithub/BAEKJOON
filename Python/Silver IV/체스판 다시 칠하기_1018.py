import sys
input=sys.stdin.readline
print=sys.stdout.write

N,M=map(int,input().rstrip().split())
chess=[[0 for i in range(M)]for j in range(N)]
for i in range(N):
    chess[i]=list(input().rstrip())

count=[]
a,b=0,0
while a<N-7 and b<M-7:
    num=0
    for i in range(a,a+8):
        for j in range(b,b+8):
            if (i+j)%2==0:
                if chess[i][j]=='B':
                    num+=1
            else:
                if chess[i][j]=='W':
                    num+=1
    if b<M-8:
        b+=1
    elif b==M-8:
        b=0
        a+=1
    count.append(num)

a,b=0,0
while a<N-7 and b<M-7:
    num=0
    for i in range(a,a+8):
        for j in range(b,b+8):
            if (i+j)%2==0:
                if chess[i][j]=='W':
                    num+=1
            else:
                if chess[i][j]=='B':
                    num+=1
    if b<M-8:
        b+=1
    elif b==M-8:
        b=0
        a+=1
    count.append(num)
print(f"{min(count)}")


# #white start
# count1=0
# for i in range(N):
#     for j in range(M):
#         if (i+j)%2==0:
#             if chess[i][j]=='B':
#                 chess[i][j]='W'
#                 count1+=1
#         else:
#             if chess[i][j]=='W':
#                 chess[i][j]='B'
#                 count1+=1
# print(f"{count1}")

# #black start
# count2=0
# for i in range(N):
#     for j in range(M):
#         if (i+j)%2==0:
#             if chess[i][j]=='W':
#                 chess[i][j]='B'
#                 count1+=1
#         else:
#             if chess[i][j]=='B':
#                 chess[i][j]='W'
#                 count1+=1
# print(f"{count2}")