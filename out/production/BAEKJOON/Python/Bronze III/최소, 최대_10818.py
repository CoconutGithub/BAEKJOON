import sys
input=sys.stdin.readline
print=sys.stdout.write

N=input().rstrip()
num=list(map(int,input().rstrip().split()))
print(f"{min(num)} {max(num)}\n")