T = int(input())

for tc in range (T):
    N, M, K = map(int, input().split())
    
    board = [list(map(int, input().split())) for _ in range (N)]
    cell_dict = {}
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    # 줄기세포 정보 딕셔너리에 입력 [활성되기까지 시간, 사망까지 시간, 고유]
    for i in range (N):
        for j in range (M):
            if board[i][j] > 0:
                num = board[i][j]
                cell_dict[i, j] = [num, num, num]
    
    def sol(x, y): # 활성화하고 1시간 동작
        for ii in range (4):
            nx = (x[0] + dx[ii], x[1] + dy[ii])
            if (nx not in cell_dict) and (nx not in tem_dict or tem_dict[nx][2] < y):
                tem_dict[nx] = [y, y, y]
    tt = 0
    while tt < K:
        # 1시간마다 시간 감소로 활성화, 만약 활성화 된상태면 사망시간 흘러감
        for v in cell_dict.values():
            if v[0] > 0:
                v[0] -= 1
            elif v[0] == 0 and v[1] > -1:
                v[1] -= 1
    
        # 사망 상태가 되면 sol 이동
        tem_dict = {}
        for i, v in cell_dict.items():
            if v[1] == v[2] - 1:
                sol(i, v[2])
        if tem_dict:
            cell_dict.update(tem_dict)
    
        tt += 1
 
    ans = 0
    for v in cell_dict.values():
        if v[1] > 0:
           ans += 1     
        
    print (f"#{tc+1} {ans}")