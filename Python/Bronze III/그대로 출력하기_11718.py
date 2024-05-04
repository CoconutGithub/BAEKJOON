import sys
input=sys.stdin.readline
print=sys.stdout.write

while 1:
    string=""
    try:
        string=input()
        if(string==""):
            break
        print(f"{string}")
    except:
        break
