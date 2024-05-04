import sys
input=sys.stdin.readline
print=sys.stdout.write

N,B=map(int,input().rstrip().split())
alphabet={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'J',20:'K',21:'L',22:'M',23:'N',24:'O',25:'P',26:'Q',27:'R',28:'S',29:'T',30:'U',31:'V',32:'W',33:'X',34:'Y',35:'Z'}

num=[]
while N>=B:
    if (N%B>9):
        num.append(alphabet[N%B])
        N=N//B
    else:
        num.append(N%B)
        N=N//B
if(N>9):
    num.append(alphabet[N])
else:
    num.append(N)
num=num[::-1]

for i in num:
    print(f"{i}")