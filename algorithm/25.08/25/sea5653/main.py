import sys
sys.stdin = open('sample_input (10).txt','r')

T = int(input())


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cell_dict = {}
for i in range(n):
    for j in range(m):
        if board[i][j]:
            num = board[i][j]
            cell_dict[(i, j)] = [num, num, num]

print (cell_dict)
xxx = 3
while xxx:
    for pos, val in cell_dict.items():
        if val[0]:  # 비활성화 상태
            val[0] -= 1
        else:
            if val[1]:   # 활성 상태
                val[1] -= 1

        new_cell = {}
        if val[1] == val[2] - 1:
            x = pos[0]
            y = pos[1]
            print (xxx, x, y)
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if (nx, ny) not in cell_dict:
                    print(xxx, x, y, "hi")
                    if (nx, ny) not in new_cell:
                        num = val[2]
                        new_cell[(nx, ny)] = [num, num, num]
                    else:
                        num = max(new_cell[(nx, ny)][2], val[2])
                        new_cell[(nx, ny)] = [num, num, num]

    if new_cell:
        cell_dict.update(new_cell)
    print (xxx, cell_dict)
    xxx -= 1

cnt = 0
for val in cell_dict.values():
    if val[0] > 0 or val[1] > 0:
        cnt += 1

print(cnt)