X=int(input())

binary=int(format(X,'b'))
count=0
while(binary>0):
    if(binary%10==1):
        count+=1
        binary=binary//10
    else:
        binary=binary//10
print(count)
#2진수 문제