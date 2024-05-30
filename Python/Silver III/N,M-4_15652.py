from sys import stdin
input=stdin.readline

n,m=map(int,input().rstrip().split())
l=[]

def bt(st):
    if len(l)==m:
        print(' '.join(map(str,l)))#리스트 길이가 m이 됐다면 다 출력
        return
    for i in range(st,n+1):
        l.append(i)#1부터 n까지 넣음
        bt(i)#i부터 시작되는 수 채우기
        l.pop()#앞 부분은 바꾸지 않고 뒤를 계속 바꿔 나가기 위해 pop
bt(1)#1부터
