import sys
input=sys.stdin.readline
print=sys.stdout.write

a=[]
for i in range(10):
    a.append((int(input().rstrip()))%42)
# count=[]
# for i in a:
#     if i not in count:
#         count.append(i)
# print(f"{len(count)}")
print(f"{len(set(a))}")

