import sys
sys.stdin = open('sample_input (22).txt','r')


import heapq

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    heap = []
    for x in nums:
        heapq.heappush(heap, x)

    ans = 0
    v = n - 1
    while v > 0:
        v = (v - 1) // 2
        ans += heap[v]

    print(f"#{tc} {ans}")