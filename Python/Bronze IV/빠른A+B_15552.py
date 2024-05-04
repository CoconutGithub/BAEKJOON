import sys
input=sys.stdin.readline
print=sys.stdout.write

plus=int(input())
for i in range(plus):
    temp=input().rstrip().split()
    print(f"{int(temp[0])+int(temp[1])}\n")
#빠른 입출력 공부