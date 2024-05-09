N=int(input())
word=[]
for i in range(N):
    word.append(input())
word.sort()#알파펫 정렬
word.sort(key=len)#길이 정렬
#set은 순서가 바뀌는거 때문에 for문 돌림
result=[]
for i in word:
    if i not in result:
        result.append(i)
for i in result:
    print(i)