import sys
sys.stdin = open('taek/algorithm/25.10/07/하나로/re_sample_input.txt','r')


import heapq

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    x_pos = list(map(int, input().split()))
    y_pos = list(map(int, input().split()))
    pos_list = list(zip(x_pos, y_pos))
    e = float(input())

    visited = set()
    adj_list = {i:{} for i in range(n+1)}

    for i in range(n):
        for j in range(i+1, n):
            dx = pos_list[i][0] - pos_list[j][0]
            dy = pos_list[i][1] - pos_list[j][1]
            dist = (dx*dx) + (dy*dy)

            adj_list[i][j] = dist
            adj_list[j][i] = dist

    mst_weight = 0

    min_heap = []
    heapq.heappush(min_heap, [0, 0])

    while min_heap:
        val, x = heapq.heappop(min_heap)

        if x in visited:
            continue

        visited.add(x)
        mst_weight += val

        for nx, weight in adj_list[x].items():
            if nx not in visited:
                heapq.heappush(min_heap, [weight, nx])

        if len(visited) == n:
            break

    print (f"#{tc} {round(mst_weight*e)}")