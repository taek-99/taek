T = int(input())

for tc in range (T):
    n, m, k = map(int,input().split())
    bug_list = [list(map(int, input().split())) for _ in range (k)]
    bug_map = [[0] * n for _ in range (n)]
    bug_pos = []
    bug_cnt = []
    bug_dir = []
    
    # 상하좌우 숫자에 맞춰서 설정
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]


    # 군집끼리 만났을 때 동작
    def sol_meet():
        for ii in range(len(bug_pos)):  
            sum_bug = []
            x = bug_pos[ii][0]
            y = bug_pos[ii][1]
    
            sum_bug = [l for l, val in enumerate(bug_pos) if val[0] == x and val[1] == y]
    
            # 겹치는 군집이 두 무리 이상 일때
            if len(sum_bug) > 1:
                bug_max = max(sum_bug, key=lambda l : bug_pos[l][2])
                for jj in sum_bug:
                    if bug_max != jj:
                        bug_pos[bug_max][2] += bug_pos[jj][2]
                        bug_pos[jj][2] = 0   
    
    
    # outline에 갔을 경우 반 사망 후 방향 바뀜
    def sol_outline(x, y, z, ii):
        if bug_map[x][y] == -999:
            bug_pos[ii][2] = bug_pos[ii][2] // 2
            if z == 1:            
                bug_pos[ii][3] = 2
            elif z == 2:            
                bug_pos[ii][3] = 1
            elif z == 3:            
                bug_pos[ii][3] = 4
            else:            
                bug_pos[ii][3] = 3
                
    # 전체적인 이동
    def sol_move():
        for ii in range(len(bug_pos)):
            x = bug_pos[ii][0]
            y = bug_pos[ii][1]
            z = bug_pos[ii][3]
            nx = x + dx[z]
            ny = y + dy[z]
            sol_outline (nx, ny, z, ii)
            bug_pos[ii][0] = nx
            bug_pos[ii][1] = ny
    
    # 가장 자리 -999
    for i in range (n):
        for j in range (n):
            if i == 0 or i == (n-1):
                bug_map[i][j] = -999
            if j == 0 or j == (n-1):
                bug_map[i][j] = -999
    
    for i in range (k):
        bug_pos.append([bug_list[i][0], bug_list[i][1], bug_list[i][2], bug_list[i][3]])
    
    for i in range (m):
        sol_move()
        sol_meet()
    
    ans = 0
    for i in range (len(bug_pos)):
        ans += bug_pos[i][2]
    
    print (f"#{tc+1} {ans}")