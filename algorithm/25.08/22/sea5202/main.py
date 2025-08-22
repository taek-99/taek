import sys
sys.stdin = open('sample_input (7).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = [list(map(int, input().split())) for _ in range(n)]

    nums.sort(key=lambda x: x[1])

    run = nums[0][1]
    ans = 1
    for st, ed in nums:
        if st >= run:
            ans += 1
            run = ed

    print (f"#{tc} {ans}")