import sys
input=sys.stdin.readline
print=sys.stdout.write

#루프 탈출 조건이 없어서 예외처리로 종료하도록 만듦
a=1
b=1
while 1:
    try:
        a,b=map(int,input().rstrip().split())
        print(f"{a+b}\n")
    except:
        break