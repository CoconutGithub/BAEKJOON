import sys
input=sys.stdin.readline
print=sys.stdout.write

test=int(input().rstrip())
for i in range(test):
    string=input().rstrip()
    print(f"{string[0]}{string[-1]}\n")