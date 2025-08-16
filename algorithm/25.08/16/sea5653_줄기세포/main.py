# 11:10

T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    cell_dict = {}
    
    for i in range(n): # 딕셔너리 입력 (활성화, 사망, 고유)
        for j in range(m):
            if board[i][j]:
                num = board[i][j]
                cell_dict[(i,j)] = [num, num, num] 
    
    while k:
        # 세포시간 흐름
        new_cell_dict = {}
        for pos, cell in cell_dict.items():
            if cell[0] > 0: # 비활성화 시간
                cell[0] -= 1 
            elif cell[0] == 0 and cell[1] > 0: # 활성 시간
                cell[1] -= 1
            
        
            if cell[0] == 0 and cell[1] == cell[2]-1:
                for ii in range(4):
                    nx = pos[0] + dx[ii]
                    ny = pos[1] + dy[ii]
                    if (nx, ny) not in cell_dict:
                        if (nx, ny) not in new_cell_dict:
                            num = cell[2]
                            new_cell_dict[(nx,ny)] = [num, num, num]
                        elif new_cell_dict[(nx, ny)][2] < cell[2]:
                            num = cell_dict[cell][2]
                            new_cell_dict[(nx,ny)] = [num, num, num]
                        
            if cell[0] == 0 and cell[1] == 0: # 사망 처리
                cell[2] = 0
    
                        
            # print (cell, cell_dict[cell][0], cell_dict[cell][1], cell_dict[cell][2])
        if new_cell_dict:
            cell_dict.update(new_cell_dict)
        # print (new_cell_dict)
        # print (k, "========================")
        k -= 1
    
    cnt = 0
    for cell in cell_dict:
        if cell_dict[cell][2] > 0:
            cnt += 1
    
    print (f"#{tc} {cnt}")

        