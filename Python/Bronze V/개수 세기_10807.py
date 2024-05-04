import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
array=input().rstrip().split()
target=input().rstrip()
print(f"{array.count(target)}\n")