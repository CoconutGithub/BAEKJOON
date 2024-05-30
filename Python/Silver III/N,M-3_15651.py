from sys import stdin
input=stdin.readline
from itertools import product

n,m=map(int,input().rstrip().split())
l=[]

def bt(n,m):
    if len(l)==m:
        print(' '.join(map(str,l)))#리스트 길이가 m이 됐다면 다 출력
        return
    for i in range(1,n+1):
        l.append(i)#1부터 n까지 넣음
        bt(n,m)#똑같이 1~n까지 넣고 m길이 가 될 때 까지 반복
        l.pop()#앞 부분은 바꾸지 않고 뒤를 계속 바꿔 나가기 위해 pop
    
bt(n,m)

# l=[i for i in range(1,n+1)]
# rs=list(product(l,l))#순열 문제 n에서 m개의 숫자 뽑아서 조합
# for i in rs:
#     tmp=str(i)
#     tmp=tmp.replace("(","")
#     tmp=tmp.replace(")","")
#     tmp=tmp.replace(",","")
#     print(tmp)