import sys
sys.stdin = open('input (8).txt','r')

import heapq

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    heap_board = [[float('inf')] * n for _ in range(n)]
    heap_board[0][0] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    min_heap = []

    heapq.heappush(min_heap, [0, (0, 0)])

    while min_heap:
        distance, (x, y) = heapq.heappop(min_heap)

        if heap_board[x][y] < distance:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not(0 <= nx < n and 0 <= ny < n):
                continue

            next_distance = distance + board[nx][ny]
            if next_distance < heap_board[nx][ny]:
                heap_board[nx][ny] = next_distance
                heapq.heappush(min_heap, [next_distance, (nx, ny)])

    print(f"#{tc} {heap_board[n-1][n-1]}")

