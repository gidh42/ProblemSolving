import sys
n = int(sys.stdin.readline())
list=[]
for i in range(n):
    x, y = map(int, input().split())
    list.append([y, x])

s_list = sorted(list)

for y,x in s_list:
    print(x,y)

# for j in range(n):
#     print(s_list[j][1], s_list[j][0])
