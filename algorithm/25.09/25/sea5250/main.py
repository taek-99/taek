import sys
sys.stdin = open('sample_input (20).txt','r')

import heapq

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    heapq_board = [[float('inf')] * n for _ in range(n)]
    heapq_board[0][0] = 0
    min_heap = []

    heapq.heappush(min_heap, [0, (0, 0)])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while min_heap:
        v, (x, y) = heapq.heappop(min_heap)

        if heapq_board[x][y] < v:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            high = board[nx][ny] - board[x][y]
            distance = v + 1 + max(0, high)
            if distance < heapq_board[nx][ny]:
                heapq_board[nx][ny] = distance
                heapq.heappush(min_heap, [distance, (nx, ny)])

    print(f"#{tc} {heapq_board[n-1][n-1]}")