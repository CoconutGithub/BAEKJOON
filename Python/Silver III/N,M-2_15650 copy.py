from sys import stdin
input=stdin.readline
from itertools import combinations

n,m=map(int,input().rstrip().split())
fac=1
for i in range(m):
    fac*=n-i
l=[i for i in range(1,n+1)]

rs=list(combinations(l,m))#순열 문제 n에서 m개의 숫자 뽑아서 조합
for i in rs:
    tmp=str(i)
    tmp=tmp.replace("(","")
    tmp=tmp.replace(")","")
    tmp=tmp.replace(",","")
    print(tmp)
