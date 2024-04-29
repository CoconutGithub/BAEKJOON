import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
age=[]
name=[]
for i in range(N):
    temp=(input().rstrip().split())
    age.append(int(temp[0]))
    name.append(temp[1])
for i in range(N):
    for j in range(1,N):
        if age[j]<age[j-1]:
            age[j],age[j-1]=age[j-1],age[j]
            name[j],name[j-1]=name[j-1],name[j]
for i in range(N): 
    print(f"{age[i]} {name[i]}\n")