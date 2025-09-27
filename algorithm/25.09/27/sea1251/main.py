import sys
sys.stdin = open('taek/algorithm/25.09/27/sea1251/re_sample_input.txt','r')

import heapq

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    x_pos = list(map(int, input().split()))
    y_pos = list(map(int, input().split()))
    e = float(input())
    node = list(zip(x_pos, y_pos))
    visited = set()
    
    adj_list = {i: [] for i in range(n)}
    vertices = list(range(n))

    def prim(vertices, adj_list):
        visited = set()
        min_heap = []
        heapq.heappush(min_heap, (0, vertices[0]))
        mst_weight = 0

        while min_heap:
            weight, pos = heapq.heappop(min_heap)

            if pos in visited:
                continue
                
            visited.add(pos)
            mst_weight += weight

            for v, w in adj_list[pos]:
                if v not in visited:
                    heapq.heappush(min_heap, (w, v))

            if len(visited) == n:
                break

        return mst_weight

    for i in range(n):
        for j in range(i+1, n):
            dx = node[i][0] - node[j][0]
            dy = node[i][1] - node[j][1]
            dist = (dx*dx) + (dy*dy)

            adj_list[i].append((j, dist))
            adj_list[j].append((i, dist))

    min_cost = prim(vertices, adj_list)

    print (f"#{tc} {round(min_cost*e)}")