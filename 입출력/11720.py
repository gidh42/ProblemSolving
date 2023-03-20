import sys
n = sys.stdin.readline()
num = sys.stdin.readline()
total = 0
for i in range(int(n)):
    total += int(num[i])
print(total)