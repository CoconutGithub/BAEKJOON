import sys
input=sys.stdin.readline
print=sys.stdout.write

matrix=[['' for i in range(5)]for j in range(15)]

for i in range(5):
    temp=input().rstrip()
    for j in range(len(temp)):
        matrix[j][i]=temp[j]

for i in range(15):
    for j in range(5):
        print(f"{matrix[i][j]}")
