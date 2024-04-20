import sys
input=sys.stdin.readline
print=sys.stdout.write

num=int(input().rstrip())
for i in range(1,num+1):
    space=num-i
    star=2*i-1
    print(f" "*space)
    print(f"*"*star+"\n")
for i in range(num-1,0,-1):
    star=2*i-1
    space=num-i
    print(f" "*space)
    print(f"*"*star+"\n")
