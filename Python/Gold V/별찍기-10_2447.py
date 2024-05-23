from sys import stdin
input=stdin.readline
from math import log


n=int(input().rstrip())
k=int(log(n,3))

def star(n):
    if n==1:
        return ['*']
    stars=star(n//3)
    l=[]
    for i in stars:
        l.append(i*3)
    for i in stars:
        l.append(i+' '*(n//3)+i)
    for i in stars:
        l.append(i*3)
    return l
for i in star(n):
    print(i)
# s="***"
# h="* *"
# b="   "
# N='\n'
# # n=3 k=1 n=9 k=2 n=27 k=3
# star=""
# if k>1:
#     for i in range(n):
#         if i>=n//3 and i<(n//3)*2:
#             if i%3==0 or i%3==2:
#                 star+=s*(n//9)+b*(n//9)+s*(n//9)+N
#             else:
#                 star+=h*(n//9)+b*(n//9)+h*(n//9)+N
#         else:
#             if i%3==0 or i%3==2:
#                 star+=s*(n//3)+N
#             else:
#                 star+=h*(n//3)+N
# else:
#     star+=s+N+h+N+s




