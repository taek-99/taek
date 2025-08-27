import sys
sys.stdin = open('taek/algorithm/25.08/27/sea2112/sample_input (35).txt','r')

T = int(input())

for tc in range(1, T+1):
    d, w, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(d)]
    zero_num = [0] * w
    one_num = [1] * w


    if k == 1:
        print (f"#{tc} 0")
        continue

    def bond_test(bd):
        for i in range(w):
            cnt = 1
            visited = False
            for j in range(d-1):
                if bd[j][i] == bd[j+1][i]:
                    cnt += 1
                else:
                    cnt = 1
                
                if cnt >= k:  # 연속으로 3개 같으면 다음 열 검사
                    visited = True
                    break
                
            if not visited:
                return False    
        return True  # 테스트 모두 통과하면 True 반환


    def dfs(idx, used):
        global best

        if used >= best:  # 사용 횟수가 최고 횟수보다 많아지면 더이상 검사 x
            return
        
        if bond_test(board): # test 진행
            best = used
            return
        
        if idx == d:
            return
        
        zero_list = all(val == 0 for val in board[idx])
        one_list = all(val == 1 for val in board[idx])
        saved = board[idx]

        dfs(idx+1, used)

        if not zero_list:
            board[idx] = zero_num
            dfs (idx+1, used+1)

        if not one_list:
            board[idx] = one_num
            dfs (idx+1, used+1)

        board[idx] = saved


    best = k+1
    dfs(0, 0)

    print (f"#{tc} {best}")