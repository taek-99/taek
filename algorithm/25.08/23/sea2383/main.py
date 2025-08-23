import sys
sys.stdin = open('taek/algorithm/25.08/23/sea2383/sample_input (30).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split()))for _ in range(n)]

    stair_pos = []
    men_pos = []
    for i in range(n):  # 계단위치와 사람 위치 파악
        for j in range(n):
            if board[i][j] == 1:
                men_pos.append((i, j))
            elif board[i][j] > 1:
                stair_pos.append((i, j, board[i][j]))


    outter = []
    for x, y in men_pos:  # 사람별 각 계단 까지의 거리 파악
        a_stair = abs(x-stair_pos[0][0]) + abs(y-stair_pos[0][1]) + 1
        b_stair = abs(x-stair_pos[1][0]) + abs(y-stair_pos[1][1]) + 1
        outter.append((a_stair, b_stair))


    def sol(pos, data):
        if not pos:  # 비어있으면 할게 없음
            return 0
        
        pos.sort()  # 오름차순 하고
        max_time = max(pos[:3]) + data  # 기다려야하는 시간

        for i in range(3, len(pos)):
            max_time = max(max_time, max((pos[i-3] + data), pos[i]) + data)
        
        return max_time


    min_num = 10 ** 10
    for i in range(2 ** len(outter)):
        a_pos = []
        b_pos = []
        for j in range(len(outter)):
            if i >> j & 1 == 1:
                a_pos.append(outter[j][0])
            else:
                b_pos.append(outter[j][1])
        
        min_num = min(min_num, max(sol(a_pos, stair_pos[0][2]), sol(b_pos, stair_pos[1][2])))


    print (f"#{tc} {min_num}")