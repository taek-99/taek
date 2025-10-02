import sys
sys.stdin = open('sample_input (25).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, a, b = map(int, input().split())
    B = [[0 for _ in range(a + 1)] for _ in range(n+1)]

    for i in range(n + 1):
        for j in range(min(i, a) + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]

    print(f"#{tc} {B[n][a]}")