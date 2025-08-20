import sys
sys.stdin = open('sample_input (28).txt','r')

from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        for idx in combinations(nums, i):
            if sum(idx) == k:
                ans += 1

    print (f"#{tc} {ans}")