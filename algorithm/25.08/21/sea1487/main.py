import sys
sys.stdin = open('sample_input (2).txt','r')


from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    nums = list(range(1, 13))

    cnt = 0
    for comb in combinations(nums, n):
        if sum(comb) == k:
            cnt += 1

    print (f"#{tc} {cnt}")
