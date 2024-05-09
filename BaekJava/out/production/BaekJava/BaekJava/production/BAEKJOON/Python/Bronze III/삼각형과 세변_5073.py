import sys
input=sys.stdin.readline
print=sys.stdout.write

while 1:
    triangle=list(map(int,input().rstrip().split()))
    if 0 in triangle:
        break
    if max(triangle)>=sum(triangle)/2:
        print("Invalid\n")
    elif triangle[0]==triangle[1] and triangle[1]==triangle[2]:
        print("Equilateral\n")
    elif triangle[0]==triangle[1] or triangle[1]==triangle[2] or triangle[2]==triangle[0]:
        print("Isosceles\n")
    else:
        print("Scalene\n")