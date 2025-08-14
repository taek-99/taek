## 14:12
## 14:18

import sys
sys.stdin = open('input (23).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    nums.sort()

    max_len = 0
    for i in range(n):
        ans_list = []
        ans_list.append(nums[i])
        for j in range(i+1, n):
            if nums[j] - nums[i] <= k:
                ans_list.append(nums[j])
        max_len = max(len(ans_list), max_len)

    print (f"#{tc} {max_len}")