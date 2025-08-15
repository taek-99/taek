import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

max_count = 0

def dfs(x, y, visited_mask, count):
    global max_count
    max_count = max(max_count, count)

    if max_count == 26:
        return  # 가지치기: 알파벳은 26개뿐이므로 더 이상 탐색 불필요

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < r and 0 <= ny < c:
            next_char = board[nx][ny]
            bit = 1 << (ord(next_char) - ord('A'))
            if not (visited_mask & bit):
                dfs(nx, ny, visited_mask | bit, count + 1)

start_bit = 1 << (ord(board[0][0]) - ord('A'))
dfs(0, 0, start_bit, 1)
print(max_count)