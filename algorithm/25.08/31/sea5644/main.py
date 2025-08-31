import sys
sys.stdin = open('taek/algorithm/25.08/31/sea5644/sample_input (38).txt','r')

from collections import defaultdict, deque
T = int(input())

for tc in range(1, T+1):
    n, a = map(int, input().split())
    a_phone_dir = list(map(int, input().split()))
    b_phone_dir = list(map(int, input().split()))
    ap_list = [list(map(int, input().split())) for _ in range(a)]
    board = [[[] for _ in range(10)] for _ in range(10)]
    charge_num = []


    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, 1, 0, -1]


    for idx in range(a):
        col = ap_list[idx][0]
        row = ap_list[idx][1]
        k = ap_list[idx][2]
        num = ap_list[idx][3]
        charge_num.append(num)

        dq = deque()
        new_dq = deque()
        pos_list = set()
        new_dq.append((row-1, col-1))
        pos_list.add((row-1, col-1))
        for _ in range(k+1):
            dq = new_dq
            new_dq = deque()
            while dq:
                x, y = dq.popleft()
                board[x][y].append(idx)
                for d in range(1, 5):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if (nx, ny) not in pos_list:
                        if not(0 <= nx < 10 and 0 <= ny < 10):
                            continue

                        new_dq.append((nx, ny))
                        pos_list.add((nx, ny))


    def sol(a_idx, b_idx):

        a_cands = (a_idx[:] if a_idx else []) + [-1]
        b_cands = (b_idx[:] if b_idx else []) + [-1]

        best_sum = -1
        best_gain = (0, 0)

        for ai in a_cands:
            for bi in b_cands:
                if ai == -1 and bi == -1:
                    a_gain = b_gain = 0
                elif ai != -1 and bi != -1 and ai == bi:
                    share = charge_num[ai] // 2
                    a_gain = share
                    b_gain = share
                else:
                    a_gain = charge_num[ai] if ai != -1 else 0
                    b_gain = charge_num[bi] if bi != -1 else 0

                s = a_gain + b_gain
                if s > best_sum:
                    best_sum = s
                    best_gain = (a_gain, b_gain)

        return best_gain

    a_phone = []
    b_phone = []
    ax = 0
    ay = 0
    bx = 9
    by = 9
    for tt in range(n+1):

        a_pos = board[ax][ay]
        b_pos = board[bx][by]
        
        a_gain, b_gain = sol(a_pos, b_pos)
        a_phone.append(a_gain)
        b_phone.append(b_gain)

        if tt < n:
            ax = ax + dx[a_phone_dir[tt]]
            ay = ay + dy[a_phone_dir[tt]]
            bx = bx + dx[b_phone_dir[tt]]
            by = by + dy[b_phone_dir[tt]]


    print (f"#{tc} {sum(a_phone) + sum(b_phone)}")