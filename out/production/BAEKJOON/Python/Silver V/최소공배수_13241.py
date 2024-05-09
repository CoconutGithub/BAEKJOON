import sys
input=sys.stdin.readline
print=sys.stdout.write

result=[]
A,B=map(int,input().rstrip().split())
if A==1 or B==1:
    result.append(A*B)
else:
    num=2
    product=1
    while A>1 or B>1:
        if A%num==0 and B%num==0:
            product*=num
            A//=num
            B//=num
        elif A%num==0:
            product*=num
            A//=num
        elif B%num==0:
            product*=num
            B//=num
        else:
            num+=1
    result.append(product)
for i in result:
    print(f"{i}\n")