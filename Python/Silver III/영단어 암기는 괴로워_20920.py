from sys import stdin
input=stdin.readline

n,m=map(int,input().rstrip().split())

# word=[]
# for _ in range(n):#일정길이 이상 단어만 받기
#     temp=input().rstrip()
#     if len(temp)>=m:
#         word.append(temp)

# dic=dict()
# for i in word:#각 단어 개수를 키값으로 갖는 딕셔너리 생성
#     if word.count(i) in dic:
#         dic[word.count(i)].append(i)
#     else:
#         dic[word.count(i)]=[i]

# result=[]
# for i in range(max(dic),0,-1):#딕셔너리 최대 키값부터 받아오기
#     temp=sorted(list(set(dic[i])))#알파벳순으로 먼저 정리
#     temp.sort(key=len, reverse=True)#단어 길이 긴 순으로 정리
#     for j in temp:
#         result.append(j)
# for i in result:
#     print(i)
dic=dict()
for i in range(n):
    s=input().rstrip()
    if dic.get(s):
        dic[s]+=1
    else:
        if len(s)>=m:
            dic[s]=1
for a,b in sorted(dic.items(),key=lambda x:(-x[1],-len(x[0]),x[0])):
    #lambda는 정렬 기준을 여러개 사용할 때 사용
    #딕셔너리를 a,b로 받아서 키는 a, 밸류는 b로 받음
    #람다 조건의 x[0]은 키, x[1]은 밸류가 됨
    #처음에 밸류가 높은순으로 정렬(단어가 많이 나온 순)
    #두번째로 길이가 긴 순으로 정렬
    #세번째로 알파벳 순으로 정렬
    print(a)