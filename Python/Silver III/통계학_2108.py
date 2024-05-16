from sys import stdin
input=stdin.readline

n=int(input().rstrip())
num=[]
for _ in range(n):
    num.append(int(input().rstrip()))
    
print(round(sum(num)/n))

print(sorted(num)[n//2])

cnt=dict()
mval=0
mkey=[]
for i in num:
    if i not in cnt:
        cnt[i]=1
    else:
        cnt[i]+=1
for i in cnt.values():
    if i>mval:
        mval=i
for i in cnt:
    if cnt[i]==mval:
        mkey.append(i)
if len(mkey)>1:
    mkey.remove(min(mkey))
    print(min(mkey))
else:
    print(mkey.pop())

print(max(num)-min(num))