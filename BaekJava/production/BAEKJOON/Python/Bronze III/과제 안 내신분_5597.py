import sys
input=sys.stdin.readline
print=sys.stdout.write

temp=[i+1 for i in range(30)]

for i in range(28):
    num=int(input().rstrip())
    if num in temp:
        temp.remove(num)
for i in temp:
    print(f"{i}\n")

#이름 변경 커밋
