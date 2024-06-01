from sys import stdin
input=stdin.readline

t=int(input().rstrip())#테스트 케이스 입력
for _ in range(t):
    n=int(input().rstrip())#몇번째 삼각형 길이 출력할지 입력
    l=[''for i in range(100)]#n이 100까지라 100개 생성
    l[0],l[1],l[2]=1,1,1#처음 6개는 미리 넣어놓음
    l[3],l[4]=2,2
    l[5]=3
    for i in range(6,n):#7번째 삼각형부터는 사실상 피보나치랑 똑같음
        l[i]=l[i-1]+l[i-5]

    print(l[n-1])
