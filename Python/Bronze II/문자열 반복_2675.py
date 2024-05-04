import sys
input=sys.stdin.readline
print=sys.stdout.write

T=int(input().rstrip())
for i in range(T):
    R,S=map(str,input().rstrip().split())
    R=int(R)
    for j in range(len(S)):
        print(f"{S[j]*R}")
    print('\n')
    
    