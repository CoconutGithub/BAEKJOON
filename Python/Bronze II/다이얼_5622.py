import sys
input=sys.stdin.readline
print=sys.stdout.write

string=input().rstrip()
time=0

for i in string:
    if(ord(i)>=65 and ord(i)<68):
        time+=3
    elif(ord(i)>=68 and ord(i)<71):
        time+=4
    elif(ord(i)>=71 and ord(i)<74):
        time+=5
    elif(ord(i)>=74 and ord(i)<77):
        time+=6
    elif(ord(i)>=77 and ord(i)<80):
        time+=7
    elif(ord(i)>=80 and ord(i)<84):
        time+=8
    elif(ord(i)>=84 and ord(i)<87):
        time+=9
    elif(ord(i)>=87 and ord(i)<91):
        time+=10
    else:
        time+=11
print(f"{time}")