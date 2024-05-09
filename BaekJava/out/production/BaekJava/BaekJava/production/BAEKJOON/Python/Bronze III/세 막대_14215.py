import sys
input=sys.stdin.readline
print=sys.stdout.write

stick=list(map(int,input().rstrip().split()))

if(max(stick)>=sum(stick)/2):
    print(f"{(sum(stick)-max(stick))*2-1}")
else:
    print(f"{sum(stick)}")