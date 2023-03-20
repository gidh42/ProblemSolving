import sys
n = int(sys.stdin.readline())
list=[]
for i in range(n):
    [x, y] = map(int, input().split())
    list.append([x,y])

s_list = sorted(list)

for j in range(n):
    print(s_list[j][0], s_list[j][1])