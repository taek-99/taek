import sys
sys.stdin = open('taek/algorithm/25.10/07/최단경로/sample_input (41).txt','r')

import heapq

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    INF = float("inf")
    heap_board = [INF] * (n+1)
    p_list = {i:{} for i in range(n+1)}

    for _ in range(m):
        x, y, v = map(int, input().split())
        p_list[x][y] = v

    min_heap = []
    heapq.heappush(min_heap, [0, 0])
    heap_board[0] = 0

    while min_heap:
        val, x = heapq.heappop(min_heap)

        if heap_board[x] < val:
            break

        for nx, weight in p_list[x].items():
            distance = val + weight
            if distance < heap_board[nx]:
                heap_board[nx] = distance
                heapq.heappush(min_heap, [distance, nx])

    print (f"#{tc} {heap_board[n]}")