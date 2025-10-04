import sys
sys.stdin = open('sample_input (25).txt','r')


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 3
    dp[3] = 6

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] * 2 + dp[i-3]

    print(f"#{tc} {dp[n]}")