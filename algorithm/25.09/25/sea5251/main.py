import sys
sys.stdin = open('sample_input (19).txt','r')

import heapq

T = int(input())

for tc in range(1, T + 1):
    n, e = map(int, input().split())

    adj_list = {i: {} for i in range(n+1)}

    for _ in range(e):
        x, y, v = map(int, input().split())
        adj_list[x][y] = v

    INF = float('INF')
    start = 0
    distances = {v: INF for v in adj_list}
    distances[start] = 0

    min_heap = []
    heapq.heappush(min_heap, [0, start])

    while min_heap:
        v, y = heapq.heappop(min_heap)

        if distances[y] < v:
            continue

        for next_pos, weight in adj_list[y].items():
            distance = v + weight
            if distance < distances[next_pos]:
                distances[next_pos] = distance
                heapq.heappush(min_heap, [distance, next_pos])

    print(f"#{tc} {distances[n]}")