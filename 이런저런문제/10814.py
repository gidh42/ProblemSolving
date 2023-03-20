import sys
n = int(sys.stdin.readline())
user=[]
#리스트 형태로 입력
for i in range(n):
    user.append(list(input().split()))

user.sort(key=lambda a : int(a[0]))

for j in range(n):
    print(user[j][0], user[j][1])