import sys
input=sys.stdin.readline
print=sys.stdout.write

num=[]
for i in range(5):
    num.append(int(input().rstrip()))
num=sorted(num)
print(f"{sum(num)//5}\n")
print(f"{num[2]}\n")

