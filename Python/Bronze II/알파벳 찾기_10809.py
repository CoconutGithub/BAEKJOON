import sys
input=sys.stdin.readline
print=sys.stdout.write

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word=input().rstrip()
result=[]
for i in alphabet:
    if i in word:
        result.append(word.index(i))
    else:
        result.append(-1)
for i in result:
    print(f"{i} ")