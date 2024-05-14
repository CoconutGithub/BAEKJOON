from sys import stdin
input=stdin.readline
from collections import deque

n=int(input().rstrip())
balloon=deque((map(int,input().rstrip().split())))
num={}
for i in range(n):
    num[balloon[i]]=i+1
while len(balloon)>0:
    temp=balloon.popleft()
    print(num[temp],end=" ")
    if temp>0:
        balloon.rotate(-(temp-1))
    else:
        balloon.rotate(temp)
#만약 풍선 안에 중복된 숫자(인덱스는 다르고)가 있다면 dict타입 특성상
#key값이 같으면 같은 value출력이라 인덱스가 안나옴