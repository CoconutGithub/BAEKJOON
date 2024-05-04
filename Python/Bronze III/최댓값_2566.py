import sys
input=sys.stdin.readline
print=sys.stdout.write

# matrix=[[0 in range(9)]for j in range(9)]
# for i in range(9):
#     temp=list(map(int,input().rstrip().split()))
#     matrix[i]=temp
# max=0
# for i in range(9):
#     for j in range(9):
#         if matrix[i][j]>=max:
#             max=matrix[i][j]
#             index=[i,j]

# print(f"{max}\n")
# print(f"{index[0]+1} {index[1]+1}")

max_val=0
for i in range(9):
    array=list(map(int,input().rstrip().split()))
    if max(array)>=max_val:
        max_val=max(array)
        index=[i,array.index(max_val)]
print(f"{max_val}\n")       
print(f"{index[0]+1} {index[1]+1}")
