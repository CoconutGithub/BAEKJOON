import sys
input=sys.stdin.readline
print=sys.stdout.write

S=input().rstrip()
parts=[]
for i in range(1,len(S)+1):
    for j in range(len(S)):
        parts.append(S[j:j+i])
print(f"{len(set(parts))}")
