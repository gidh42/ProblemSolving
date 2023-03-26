import sys
T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    m1 = list(map(int, input().split()))
    m2 = list(map(int, input().split()))

    for i in range(1, n):
        if i == 1:
            m1[1] += m2[0]
            m2[1] += m1[0]
        else:
            m1[i] += max(m2[i-2], m2[i-1])
            m2[i] += max(m1[i-2], m1[i-1])

    print(max(m1[n-1], m2[n-1]))