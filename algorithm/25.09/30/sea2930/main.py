import sys
sys.stdin = open('sample_input (23).txt','r')

import heapq

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    ans = []
    heap = []
    heapq.heappush(heap, 1)
    for _ in range(n):
        q = list(map(int, input().split()))

        if q[0] == 1:
            heapq.heappush(heap, -q[1])
        if q[0] == 2:
            ans.append(-heapq.heappop(heap))

    result = " ".join(map(str, ans))
    print(f"#{tc} {result}")

