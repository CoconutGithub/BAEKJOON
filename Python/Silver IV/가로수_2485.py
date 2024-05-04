import sys
input=sys.stdin.readline
print=sys.stdout.write

def find_divisor(a,b):
    #유클리드 알고리즘
    while 1:
        if a%b==0:
            return b
        elif b%a==0:
            return a
        if a>b:
            a%=b
        else:
            b%=a

N=int(input().rstrip())
tree=[]
gap=[]
for i in range(N):
    tree.append(int(input().rstrip()))
for i in range(N-1):
    gap.append(tree[i+1]-tree[i])

num=gap[0]
for i in range(1,len(gap)):
    num=find_divisor(num,gap[i])
cnt=0
for i in gap:
    cnt+=(i//num)-1
print(f"{cnt}")