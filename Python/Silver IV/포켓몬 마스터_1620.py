import sys
input=sys.stdin.readline
print=sys.stdout.write

N,M=map(int,input().rstrip().split())
dic1={}
dic2={}
result=[]
for i in range(N):
    temp=input().rstrip()
    dic1[temp]=i+1
    dic2[i+1]=temp
for i in range(M):
    temp=input().rstrip()
    if temp in dic1:
        result.append(dic1[temp])
    elif int(temp) in dic2:
        result.append(dic2[int(temp)])
for i in result:
    print(f"{i}\n")