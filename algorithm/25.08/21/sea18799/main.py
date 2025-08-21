import sys
sys.stdin = open('sample_input (2).txt','r')

from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))


    ans = []
    if n == 1:
        ans.append(nums[0])
    else:
        for i in range(2, n+1):
            for idx in combinations(nums, i):
                ans.append(sum(idx) / i)

    avg = sum(ans) / len(ans)
    if avg.is_integer():
        print (f"#{tc} {int(avg)}")
    else:
        print (f"#{tc} {avg:.20f}")