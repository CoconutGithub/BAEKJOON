import sys
input=sys.stdin.readline
print=sys.stdout.write

word=input().rstrip()
count=0
for i in range(len(word)//2):
    if(word[i]==word[-(i+1)]):
        count+=1
if(count==len(word)//2):
    print("1")
else:
    print("0")