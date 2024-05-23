from sys import stdin
input=stdin.readline

def hanoi(n,start,temp,dest):#start에서 dest까지 temp를 활용해서 가기
    if n==1:
        return print(f"{start} {dest}")#1인 경우 가장 작은 블럭이기 때문에 옮기기만 하면 끝
    hanoi(n-1,start,dest,temp)#기존의 dest를 temp로 활용해서 temp까지 가장 큰 블럭빼고 다 옮기기
    print(f"{start} {dest}")#가장 큰 블럭 하나 목적지로 옮기기
    hanoi(n-1,temp,start,dest)#temp로 옮겨놨던 블럭들 목적지로 옮기기

n=int(input().rstrip())
print(2**n-1)#총 이동 수
hanoi(n,1,2,3)