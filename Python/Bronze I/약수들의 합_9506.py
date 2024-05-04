import sys
input=sys.stdin.readline
print=sys.stdout.write

while 1:
    n=int(input().rstrip())
    factor=[]
    result=""
    if(n==-1):
        break
    for i in range(1,n):
        if(n%i==0):
            factor.append(i)
    if sum(factor)==n:
        result+=f"{n} ="
        for i in factor:
            result+=f" {i} +"
        result=result.rstrip("+")
        print(f'{result}\n')
    elif sum(factor)!=n:
        print(f"{n} is NOT perfect.\n")
