from sys import stdin
input=stdin.readline

k=int(input().rstrip())
stack=[]
for _ in range(k):
    n=int(input().rstrip())
    if n==0:
        stack.pop()
    else:
        stack.append(n)
print(f"{sum(stack)}")
