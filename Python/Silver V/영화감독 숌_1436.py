import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
devil=[]
i=0
num=666
while i<N:
    if "666" in str(num):
        devil.append(num)
        i+=1
    num+=1
print(f"{devil[-1]}")