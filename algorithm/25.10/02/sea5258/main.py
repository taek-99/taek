import sys
sys.stdin = open('sample_input (24).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    dp = [0] * (n + 1)

    for weight, price in arr:
        for j in range(n, weight-1, -1):
            dp[j] = max(dp[j], dp[j-weight] + price)

    print(f"#{tc} {dp[n]}")

