T = int(input())

for tc in range (1, T+1):
    day, mon, mon3, year = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    dp = [0] * 13
    
    for m in range (1, 13):
        dp[m] = dp[m-1] + min(day * plan[m-1], mon)
    
        if m >= 3:
            dp[m] = min(dp[m], dp[m-3] + mon3)

    ans = min(dp[12], year)
    print (f"#{tc} {ans}")