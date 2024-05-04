import sys
input=sys.stdin.readline
print=sys.stdout.write

change=[25,10,5,1]

T=int(input().rstrip())

coin=[0,0,0,0]
for i in range(T):
    num=int(input().rstrip())
    for j in range(4):
        coin[j]=num//change[j]
        num%=change[j]
    for j in coin:
        print(f"{j} ")
    print('\n')