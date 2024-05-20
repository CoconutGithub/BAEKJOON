from sys import stdin
input=stdin.readline

def cantor(n):
    if n<=0:
        return '-'
    s=cantor(n-1)+' '*3**(n-1)+cantor(n-1)
    return s
    
try:
    while 1:
        n=int(input().rstrip())
        # s='-'*(3**n)
        print(cantor(n))
except:
    pass
#지렸다