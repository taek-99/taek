import sys
sys.stdin = open('sample_input (18).txt','r')

import heapq

T = int(input())

for tc in range(1, T+1):
    n, e = map(int, input().split())
    graph = {i: {} for i in range(n)}
    INF = float('inf')

    for _ in range(e):
        u, w, v = map(int, input().split())
        graph[u][w] = v

    start = 0
    distances = {v: INF for v in graph}
    distances[start] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, start])

    while min_heap:
        v, w = heapq.heappop(min_heap)

        if distances[w] < v:
            continue

        for adjacent, weight in graph[w].items():
            distance = v + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(min_heap, [distance, adjacent])

    if distances[n-1] == INF:
        print(f"#{tc} impossible")
    else:
        print(f"#{tc} {distances[n-1]}")
