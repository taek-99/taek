import sys
sys.stdin = open('sample_input (18).txt','r')

import heapq

T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())
    vertices = [i for i in range(v+1)]
    mst = []
    adj_list = {v: [] for v in vertices}

    for _ in range(e):
        x, y, w = map(int, input().split())
        adj_list[x].append((y, w))
        adj_list[y].append((x, w))


    visited = set()
    init_vertex = vertices[0]
    min_heap = [[w, init_vertex, e] for e, w in adj_list[init_vertex]]
    heapq.heapify(min_heap)
    visited.add(init_vertex)

    ans = 0

    while min_heap:
        weight, start_v, end_v = heapq.heappop(min_heap)
        if end_v in visited:
            continue

        visited.add(end_v)
        mst.append((start_v, end_v, weight))
        ans += weight

        for adj_v, adj_w in adj_list[end_v]:
            if adj_v in visited:
                continue
            heapq.heappush(min_heap, [adj_w, end_v, adj_v])

    print(f"#{tc} {ans}")