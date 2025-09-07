T = 5

for tc in range(1, T+1):
    n = 5
    k1 = 10
    k2 = 20
    nums = [i for i in range(1, n+1)]


    if sum(nums) < k1:  # 다 더해도 k1보다 작으면 진행할 필요 x
        print (-1)
        continue

    k = 2 ** n
    ans = 0
    for i in range(k):
        sum_num = 0
        for j in range(n):
            if (i >> j) & 1 == 1:
                sum_num += nums[j]
            
            if sum_num > k2:  # 가지치지 - 이미 최댓값 벗어나서 더 더할 필요 X
                break
        
        if k1 <= sum_num <= k2:
            ans += 1

    print (nums)
    print (ans)
