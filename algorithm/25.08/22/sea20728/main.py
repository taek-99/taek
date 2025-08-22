import sys
sys.stdin = open('sin.txt','r')


T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    nums.sort()
    min_num = 10 ** 10
    for i in range(n-k+1):
        diff = nums[i+k-1] - nums[i]
        min_num = min(min_num, diff)

    print (f"#{tc} {min_num}")