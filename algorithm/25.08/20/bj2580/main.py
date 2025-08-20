import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

zero_pos = []
row_used = [set() for _ in range(9)]
col_used = [set() for _ in range(9)]
box_used = [set() for _ in range(9)]


def box_idx(x, y):
    return (x//3) * 3 + (y//3)


for i in range(9): # 0인 위치 파악
    for j in range(9):
        v = board[i][j]
        if not v:
            zero_pos.append((i, j))
        else:
            row_used[i].add(v)
            col_used[j].add(v)
            box_used[box_idx(i, j)].add(v)

ALL = set(range(1, 10))


def dfs():

    best_size = 10
    target = -1
    best_cands = 0

    for idx, (x, y) in enumerate(zero_pos):
        if board[x][y] != 0:
            continue
        cands = ALL - row_used[x] - col_used[y] - box_used[box_idx(x, y)]
        sz = len(cands)
        if sz == 0:
            return False
        if sz < best_size:
            best_size = sz
            target = idx
            best_cands = cands
            if sz == 1:
                break

    if target == -1:
        for i in range(9):
            print (*board[i])
        return True

    x, y = zero_pos[target]
    b = box_idx(x, y)

    for v in sorted(best_cands):
        board[x][y] = v
        row_used[x].add(v)
        col_used[y].add(v)
        box_used[b].add(v)

        if dfs():
            return True

        board[x][y] = 0
        row_used[x].remove(v)
        col_used[y].remove(v)
        box_used[b].remove(v)

    return False


dfs ()





