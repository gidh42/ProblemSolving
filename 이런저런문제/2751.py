import sys
n = int(sys.stdin.readline())
list = []
for i in range(n):
    list.append(int(sys.stdin.readline()))

for j in sorted(list):
    print(j)