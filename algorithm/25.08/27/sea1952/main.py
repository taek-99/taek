import sys
sys.stdin = open('taek/algorithm/25.08/27/sea1952/sample_input (34).txt','r')

T = int(input())

for tc in range(1, T+1):
    one_day, one_month, thr_month, one_year = map(int, input().split())
    nums = list(map(int, input().split()))

    dp = [0] * 13

    for idx in range(1, 13):
        dp[idx] = min(nums[idx-1] * one_day, one_month) + dp[idx-1]

        if idx >= 3:
            dp[idx] = min(dp[idx], thr_month+dp[idx-3])

    print (f"#{tc} {min(dp[12], one_year)}")

        