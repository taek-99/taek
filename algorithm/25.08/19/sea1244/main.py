import sys
sys.stdin = open('input (25).txt','r')

from itertools import combinations


T = int(input())

for tc in range(1, T+1):
    nums, n = map(int, input().split())
    s0 = ''.join(map(str, str(nums)))
    level = {s0}

    nums_list = list(map(int, str(nums)))
    idx_combi = list(combinations(range(len(s0)), 2))

    for _ in range(n):
        ans_list = set()
        for s in level:
            arr = list(s)
            for a, b in idx_combi:
                arr[a], arr[b] = arr[b], arr[a]
                ans_list.add(''.join(arr))
                arr[a], arr[b] = arr[b], arr[a]
        level = ans_list

    print (f"#{tc} {max(level)}")