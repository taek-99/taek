
from collections import deque, defaultdict
import heapq

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
island_list = [[(-1, -1)] * m for _ in range(n)]
num_list = []
island_dict = defaultdict(list)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def island_contect(r, c):
    q = deque()
    q.append((r, c))
    island_dict[(r, c)].append((r, c))
    visited[r][c] = True

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
                continue

            if board[nx][ny]:    
                island_list[nx][ny] = (r, c)
                visited[nx][ny] = True
                island_dict[(r, c)].append((nx, ny))
                q.append((nx, ny))


island_cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] and not visited[i][j]:
            island_list[i][j] = (i, j)
            num_list.append((i, j))
            island_contect(i, j)
            island_cnt += 1
    


p_list = {i: [] for i in island_dict.keys()}
for val, node_list in island_dict.items():
    for (x, y) in node_list:
        for d in range(4):
            for k in range(1, max(n, m)):
                nx = x + (dx[d] * k)
                ny = y + (dy[d] * k)

                if not(0 <= nx < n and 0 <= ny < m):
                    break

                if (nx, ny) in island_dict[val]:
                    break

                if k < 3 and island_list[nx][ny] != (-1, -1):
                    break

                if k >= 3 and island_list[nx][ny] != (-1, -1):
                    for pos in island_dict.keys():
                        if (nx, ny) in island_dict[pos]:
                            p_list[val].append([(pos), k-1])
                            break
                    break



min_heap = []
island_visited = set()
heap_board = {i: float("inf") for i in island_dict.keys()}
heapq.heappush(min_heap, (0, num_list[0]))
heap_board[num_list[0]] = 0


ans = 0
while min_heap:
    w, pos = heapq.heappop(min_heap)

    if pos in island_visited:
        continue

    ans += w
    island_visited.add(pos)
    for next_pos, val in p_list[pos]:
        if next_pos not in island_visited:
            heapq.heappush(min_heap, (val, next_pos))


if len(island_visited) == len(num_list):
    print (ans)
else:
    print (-1)