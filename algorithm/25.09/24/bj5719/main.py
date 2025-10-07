import sys
sys.stdin = open('taek/algorithm/25.09/24/bj5719/input.txt')

import heapq

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break

    s_u, e_v = map(int, input().split())

    grid = [[] for _ in range(n)]

    c = [[0] * n for _ in range(n)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        
        grid[u].append(v)
        c[u][v] = w

    is_done = False
    min_v = float('inf')
    close_min_v = None

    def dijkstra():
        global is_done, min_v, close_min_v
        min_que = []
        heapq.heappush(min_que, (0, s_u, [s_u]))

        d = [float('inf')] * n
        path = [[] for _ in range(n)]
        d[s_u] = 0
        path[s_u] = [s_u]

        while min_que:
            w, u, p = heapq.heappop(min_que)

            if d[u] < w:
                continue

            for v in grid[u]:
                vw = c[u][v]
                if d[v] > vw + w:
                    d[v] = vw + w
                    path[v] = p + [v]
                    heapq.heappush(min_que, (d[v], v, path[v]))
        return d[e_v], path[e_v]

    while True:
        dist, e_path = dijkstra()
        if dist == float('inf'):
            is_done = True
        min_v = min(min_v, dist)
        for i in range(len(e_path) - 1):
            s, e = e_path[i], e_path[i+1]
            c[s][e] = float('inf')
        if dist == float('inf'):
            break
        if min_v == dist:
            continue
        close_min_v = dist
        break
    if close_min_v is None or close_min_v == float('inf'):
        print(-1)
    else:
        print(close_min_v)
