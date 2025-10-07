import sys
sys.stdin = open('taek/algorithm/25.09/28/sea1249/input (14).txt','r')


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
        val, (x, y) = heapq.heappop(min_heap)

        if heap_board[x][y] < val:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not(0 <= nx < n and 0 <= ny < n):
                continue

            disance = val + board[nx][ny]
            if disance < heap_board[nx][ny]:
                heap_board[nx][ny] = disance
                heapq.heappush(min_heap, [disance, (nx, ny)])


    print (f"#{tc} {heap_board[n-1][n-1]}")