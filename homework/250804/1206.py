for tc in range(10):
    n = int(input())
    num = list(map(int, input().split()))
     
    ans = 0
    for i in range(2, n-2):
        max_num = max(num[i-1], num[i-2], num[i+1], num[i+2])
        if num[i] > max_num:
            ans += num[i] - max_num
     
    print (f"#{tc+1} {ans}")