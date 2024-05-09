from sys import stdin
input=stdin.readline

while 1:
    line=input().rstrip()
    stack=[]
    if len(line)==1 and line[0]=='.':
        break
    for i in line:
        if i=='(':
            stack.append('(')
        elif i==')':
            try:
                if stack[-1]!='(':
                    break
                stack.pop()
            except IndexError:
                stack.append('error')
                break
        elif i=='[':
            stack.append('[')
        elif i==']':
            try:
                if stack[-1]!='[':
                    break
                stack.pop()
            except IndexError:
                stack.append('error')
                break
    if len(stack)==0:
        print("yes")
    else:
        print("no")