import sys
sys.stdin = open('taek/algorithm/25.09/27/sea1795/input (13).txt','r')

import heapq

T = int(input())

for tc in range(1, T+1):
    n, m, xx = map(int, input().split())
    adj_list = {i: {} for i in range(1, n+1)}
    reverse_adj_list = {i: {} for i in range(1, n+1)}

    for _ in range(m):
        x, y, v = map(int, input().split())
        adj_list[x][y] = v
        reverse_adj_list[y][x] = v

    def dikstra(start, graph):
        d = [float('inf')] * (n + 1)
        d[start] = 0
        queue = [(0, start)]
        while queue:
            dist, cur = heapq.heappop(queue)
            if d[cur] < dist:
                continue
            for nbr, nbr_dist in graph[cur].items():
                next_dist = dist + nbr_dist
                if d[nbr] > next_dist:
                    d[nbr] = next_dist
                    heapq.heappush(queue, (next_dist, nbr))
        return d

    max_list = dikstra(xx, adj_list)
    reverse_max_list = dikstra(xx, reverse_adj_list)
    print(f'#{tc}', max([max_list[i] + reverse_max_list[i] for i in range(1, n + 1)]))

















    # for _ in range(m):
    #     x, y, v = map(int, input().split())
    #     adj_list[x][y] = v

    # max_num = [0] * (n+1)
    # for i in range(1, n+1):
    #     min_heap = []
    #     heapq_list = {x: float('inf') for x in range(1, n+1)}
    #     heapq_list[i] = 0
    #     heapq.heappush(min_heap, [0, i])

    #     while min_heap:
    #         v, pos = heapq.heappop(min_heap)

    #         if heapq_list[pos] < v:
    #             continue

    #         for next_pos, weight in adj_list[pos].items():
    #             distance = weight + v
    #             if distance < heapq_list[next_pos]:
    #                 heapq_list[next_pos] = distance
    #                 heapq.heappush(min_heap, [distance, next_pos])

    #     max_num[i] += heapq_list[xx]
    #     if i == xx:
    #         for j in range(1, n+1):
    #             max_num[j] += heapq_list[j]

    # print (f"#{tc} {max(max_num)}")