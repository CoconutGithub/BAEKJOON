import sys
input=sys.stdin.readline
print=sys.stdout.write

string=input().rstrip().upper()
temp=list(set(string))
num_list=[]
# for i in temp:
#     num=string.count(i)
#     if(num>value):
#         value=num
#         char=i
#     elif(num==value):
#         print("?")
#         exit()
# print(char)
for i in temp:
    num_list.append(string.count(i))
if(num_list.count(max(num_list))>1):
    print("?")
else:
    print(f"{temp[num_list.index(max(num_list))]}")
