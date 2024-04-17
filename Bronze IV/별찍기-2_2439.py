import sys
input=sys.stdin.readline
print=sys.stdout.write

star=int(input().rstrip())

for i in range(1,star+1,1):
    print(" "*(star-i)+"*"*i+"\n")