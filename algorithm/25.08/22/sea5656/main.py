import sys
sys.stdin = open('sample_input (7).txt','r')


from collections import deque
T = int(input())

for tc in range(1, T+1):
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    min_num = 10 ** 10


    def bomb(x, y, bd):  # 공 부수는 중
        dq = deque()
        dq.append((x, y))
        while dq:
            bx, by = dq.popleft()
            k = bd[bx][by]
            bd[bx][by] = 0
            for ii in range(1, k):
                for d in range(4):
                    nx = bx + (dx[d] * ii)
                    ny = by + (dy[d] * ii)
                    if not (0 <= nx < h and 0 <= ny < w):
                        continue

                    if bd[nx][ny] > 0:
                        dq.append((nx, ny))


    def gravity(bd):  # 중력 작용
        for ii in range(w):
            new_list = []
            for jj in range(h-1, -1, -1):
                if bd[jj][ii]:
                    new_list.append(bd[jj][ii])
                    bd[jj][ii] = 0

            if new_list:
                for kk in range(len(new_list)):
                    bd[h-kk-1][ii] = new_list[kk]


    def dfs(shoot, brick_bd):
        global min_num

        if shoot == n + 1:  # 공 다 쐈으면 벽돌 갯수 카운팅
            ans = 0
            for i in range(h):
                for j in range(w):
                    if brick_bd[i][j]:
                        ans += 1
            min_num = min(min_num, ans)
            return

        for i in range(w):
            new_bd = [val[:] for val in brick_bd]
            for j in range(h):
                if new_bd[j][i]:
                    bomb(j, i, new_bd)  # 값이 있어서 쏨
                    gravity(new_bd)  # 중력 작용
                    dfs(shoot + 1, new_bd)
                    break
            else:
                dfs(shoot + 1, new_bd)


    dfs(1, board)

    print(f"#{tc} {min_num}")