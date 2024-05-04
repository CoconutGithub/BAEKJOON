import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
result=[]

num=2
while N>1:
    if(N%num==0):
        result.append(num)
        N//=num
    else:
        num+=1
for i in result:
    print(f"{i}\n")


