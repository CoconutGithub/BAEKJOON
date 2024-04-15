test=int(input())
m=[]
n=[]
case=[]

for i in range(test):
    temp=input().split()
    n.append(int(temp[0]))
    m.append(int(temp[1]))

def fac(n):
    num=1
    for i in range(1,n+1,1):
        num*=i
    return num

for i in range(test):
    case.append(int(fac(m[i])/(fac(n[i])*fac(m[i]-n[i]))))
    print(case[i])

#mCn