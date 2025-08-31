import sys
sys.stdin = open('25.08/31/sea5644/sample_input (38).txt','r')

from collections import defaultdict, deque
T = int(input())


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
            board[x][y].append(num)
            for d in range(1, 5):
                nx = x + dx[d]
                ny = y + dy[d]
                if (nx, ny) not in pos_list:
                    if not(0 <= nx < 10 and 0 <= ny < 10):
                        continue

                    new_dq.append((nx, ny))
                    pos_list.add((nx, ny))


a_phone = []
b_phone = []
ax = 0
ay = 0
bx = 9
by = 9
for tt in range(n):

    a_pos = board[ax][ay]
    b_pos = board[bx][by]
    
    if a_pos == b_pos and a_pos:
        if len(a_pos) == 1 and len(b_pos) == 1:
            a_phone.append(a_pos[0] // 2)
            b_phone.append(b_pos[0] // 2)
        else:
            a_pos.sort(reverse=True)
            a_phone.append(a_pos[0])
            b_phone.append(b_pos[1])
        continue

    ## 여러개중 하나만 겹칠 경우 해곃해야함

    
    if a_pos:
        a_phone.append(a_pos[0])
    if b_pos:
        b_phone.append(b_pos[0])

    ax = ax + dx[a_phone_dir[tt]]
    ay = ay + dy[a_phone_dir[tt]]
    bx = bx + dx[b_phone_dir[tt]]
    by = by + dy[b_phone_dir[tt]]

print ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print (a_phone)
print (b_phone)
print (sum(a_phone) + sum(b_phone))