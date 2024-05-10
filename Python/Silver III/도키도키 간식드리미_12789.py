from sys import stdin
input=stdin.readline

n=int(input().rstrip())
line=list(map(int,input().rstrip().split()))
temp=1
stack=[n+1]
for i in range(n*2):
    # print(f"{line}")
    # print(f"{stack}")
    # print()
    if len(line)==0 and len(stack)==1:
        print("Nice")
        break
    try:
        l=line[0]
        s=stack[-1]
    except IndexError:
        s=stack[-1]
    if l==temp:
        line.pop(0)
        temp+=1
    elif s==temp:
        stack.pop()
        temp+=1
    else:
        if l>s:
            print("Sad")
            break
        line.pop(0)
        stack.append(l)
#code feed back
