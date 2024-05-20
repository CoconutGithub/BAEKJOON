from sys import stdin
input=stdin.readline

def merge(a,start,mid,end,cnt):
    i=start
    j=mid+1
    # t=0
    # tmp=[0 for i in range(len(a))] ->이렇게하니까 시간초과남
    tmp=[]
    while i<=mid and j<=end:
        if a[i]<=a[j]:
            tmp.append(a[i])#하나씩 인덱스 늘리면서 tmp[t]=a[i]방식말고 넣어주면서 길이 지정
            # t+=1
            i+=1
        else:
            tmp.append(a[j])
            # t+=1
            j+=1
    while i<=mid:
        tmp.append(a[i])
        # t+=1
        i+=1
    while j<=end:
        tmp.append(a[j])
        # t+=1
        j+=1
    i=start
    t=0
    while i<=end:
        a[i]=tmp[t]
        cnt.append(tmp[t])
        i+=1
        t+=1

def merge_sort(a,start,end,cnt):
    if start<end:
        mid=(start+end)//2
        merge_sort(a,start,mid,cnt)
        merge_sort(a,mid+1,end,cnt)
        merge(a,start,mid,end,cnt)


n,k=map(int,input().rstrip().split())
a=list(map(int,input().rstrip().split()))
cnt=[]
merge_sort(a,0,len(a)-1,cnt)
# print(a)
if len(cnt)<k:
    print(-1)
else:
    print(cnt[k-1])
