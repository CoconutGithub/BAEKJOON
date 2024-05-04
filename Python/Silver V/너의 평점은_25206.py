import sys
input=sys.stdin.readline
print=sys.stdout.write

def change_grade(g):
    if g=="A+":
        return 4.5
    elif g=="A0":
        return 4
    elif g=="B+":
        return 3.5
    elif g=="B0":
        return 3
    elif g=="C+":
        return 2.5
    elif g=="C0":
        return 2
    elif g=="D+":
        return 1.5
    elif g=="D0":
        return 1
    elif g=="F":
        return 0
    
sum=0
num=0
for i in range(20):
    subject,point,grade=input().rstrip().split()
    if(grade=='P'):
        continue
    else:
        sum+=float(point)*change_grade(grade)
        num+=float(point)

print(f"{sum/num}")
