from sys import stdin
input=stdin.readline

n=int(input().rstrip())
cnt=0
name=set()
for _ in range(n):
    temp=input().rstrip()
    if temp=='ENTER':
        name.clear()
    elif temp not in name:
        name.add(temp)
        cnt+=1
print(cnt)