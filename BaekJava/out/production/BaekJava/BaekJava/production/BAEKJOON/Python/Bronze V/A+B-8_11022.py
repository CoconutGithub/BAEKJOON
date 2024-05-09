import sys
input=sys.stdin.readline
print=sys.stdout.write

test=int(input().rstrip())

for i in range(1,test+1,1):
    a,b=map(int,input().rstrip().split())
    print(f"Case #{i}: {a} + {b} = {a+b}\n")
