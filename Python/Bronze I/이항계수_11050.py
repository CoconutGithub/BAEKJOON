from sys import stdin
input=stdin.readline
#이항계수 = combination
#nCk=(N K)

def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac
    
n,k=map(int,input().rstrip().split())
comb=factorial(n)//(factorial(k)*factorial(n-k))
print(comb)