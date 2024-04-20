import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
count=0
for i in range(N):
    string=input().rstrip()
    word=list(set(string))
    temp=0
    for j in range(len(string)-1):
        if string[j]!=string[j+1]:
            temp+=1
    if temp+1==len(word):
        count+=1
print(f"{count}")
