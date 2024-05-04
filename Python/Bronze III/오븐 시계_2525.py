hour, min=map(int,input().split())
time=int(input())
print(f"{(hour+(min+time)//60)%24} {(min+time)%60}")