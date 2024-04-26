import sys
input=sys.stdin.readline
print=sys.stdout.write

a,b,c,d,e,f=map(int,input().rstrip().split())
if(a==0):
    y=c/b
    x=(f-e*y)/d
elif(b==0):
    x=c/a
    y=(f-d*x)/e
elif(d==0):
    y=f/e
    x=(c-b*y)/a
elif(e==0):
    x=f/d
    y=(c-a*x)/b
else:
    temp=a
    a*=d
    b*=d
    c*=d
    d*=temp
    e*=temp
    f*=temp
    if (b==e):
        y=c/b
    else:
        y=(c-f)/(b-e)
    x=(c-b*y)/a
print(f"{int(x)} {int(y)}")
