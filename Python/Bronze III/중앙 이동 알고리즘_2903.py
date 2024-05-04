import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input().rstrip())

print(f"{((2**N)+1)**2}")

# 0: 1  /  4  (1+1)**2
# 1: 4  /  9  (2+1)**2
# 2: 16 /  25 (4+1)**2