import sys
input=sys.stdin.readline
print=sys.stdout.write

alphabet=input().rstrip()
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt=0
num=0
for i in croatia:
    num=alphabet.count(i)
    if(num>0):
        alphabet=alphabet.replace(i,' ',num)
        cnt+=num
alphabet=alphabet.replace(' ','')
print(f"{len(alphabet)+cnt}")