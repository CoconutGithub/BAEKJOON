import sys
input=sys.stdin.readline
print=sys.stdout.write

N,X=map(int,input().rstrip().rsplit())
array=map(int,input().rstrip().rsplit())
temp=[]
for i in array:
    if(i<X):
        temp.append(i)
for i in temp:
    print(f"{i}\n")