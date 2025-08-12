import copy
import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split()))for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    worm_dict = {
        6 : [],
        7 : [],
        8 : [],
        9 : [],
        10 : []
    }
    
    block_dict={ # 벽 종류별 부딪혔을때 이동 방향
        1 : [1, 3, 0, 2],
        2 : [3, 0, 1, 2],
        3 : [2, 0, 3, 1],
        4 : [1, 2, 3, 0],
        5 : [1, 0, 3, 2]
    }
    
    for i in range (n): #웜홀 위치 설정/ 시작위치/ visited 설정
        for j in range(n):
            if board[i][j] > 5:
                worm_dict[board[i][j]].append((i,j))
    
    hole_dict = {}
    for i in worm_dict.values():
        if i:
            hole_dict[(i[0])] = i[1]
            hole_dict[(i[1])] = i[0] 
    
    def dfs (x, y, z):
        sx = x #시작위치 메모
        sy = y
        score = 0
        
        while True:   
            
            nx = x + dx[z]
            ny = y + dy[z]
            
            if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 5: #외곽벽에 부딪힐경우/ 4각형 벽
                score += 1
                z = block_dict[5][z]
                x, y = nx, ny
                continue

            pos = board[nx][ny]
    
            if pos == -1 or nx == sx and ny == sy: # 종료 조건 블랙홀
                break
                
    
            if 0 < pos < 5: #벽에 부딪혔을 경우
                score += 1
                x = nx
                y = ny
                z = block_dict[pos][z]
                continue
                    
            if 5 < pos < 11: #웜홀에 빠졌을 경우
                x, y = hole_dict[(nx, ny)]
                continue
        
            x = nx
            y = ny
            
        return score
                    
    max_cnt = 0
    
    for i in range (n):
        for j in range (n):
            if not board[i][j]:
                for ii in range (4):
                    ans = dfs (i, j, ii)
                    if ans > max_cnt:
                        max_cnt = ans
    
    print (f"#{tc} {max_cnt}")
    
    
    
    
    
    
    
    
    
