import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())
dic={}
for i in range(N):
    name,log=input().rstrip().split()
    dic[name]=log

enter=[]
for i in dic.keys():
    if dic[i] =='enter':
        enter.append(i)
enter=sorted(enter)[::-1]
for i in enter:
    print(f"{i}\n")
