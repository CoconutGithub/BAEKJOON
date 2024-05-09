test=int(input())
temp=[]
for i in range(test):
    a,b=map(int,input().split())
    temp.append(a+b)
for i in temp:
    print(i)