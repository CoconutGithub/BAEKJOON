from sys import stdin
input=stdin.readline

#동적 계획법 탑 다운 방식으로 품
dic=dict()
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:#종료조건 0보다 하나라도 작으면 1
        return 1
    elif a > 20 or b > 20 or c > 20:#20보다 하나라도 크면 w(20,20,20)으로 계산하기
        return w(20, 20, 20)
    
    if f"{a,b,c}" in dic:#동적 계획법의 핵심 / 이미 한번 계산한건 그냥 그대로 반환해서 계산안하기
        return dic[f"{a,b,c}"]
    
    #여기서부턴 위에서 걸러지고 새로 계산하는 놈들
    if a < b and b < c:
        dic[f"{a,b,c}"] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dic[f"{a,b,c}"]
    else:
        dic[f"{a,b,c}"] =w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dic[f"{a,b,c}"]

a,b,c=0,0,0
while 1:
    a,b,c=map(int,input().rstrip().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f"w{a,b,c} = {w(a,b,c)}")

