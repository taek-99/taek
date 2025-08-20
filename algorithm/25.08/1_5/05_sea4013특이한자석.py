from collections import deque

T = int(input())

for tc in range (T):
    k = int(input())
    
    board = [list(map(int, input().split())) for _ in range(4)]
    rotation = [list(map(int, input().split())) for _ in range(k)]
    dq_board = [deque(board[0]), deque(board[1]), deque(board[2]), deque(board[3])]

    for i in rotation:
        rot_list = []
        x = i[0] - 1
        y = i[1]
        rot_list.append((x,y))
        
        # 오른
        dy = y
        for j in range (x+1, 4, 1):
            dy *= -1
            if dq_board[j-1][2] != dq_board[j][6]:
                rot_list.append((j, dy))
            else:
                break
    
        # 왼
        dy = y
        for j in range (x-1, -1, -1):
            dy *= -1
            if dq_board[j+1][6] != dq_board[j][2]:
                rot_list.append((j, dy))
            else:
                break
    
        #회전
        for j, v in rot_list:
            dq_board[j].rotate(v)
                
    print (f"#{tc+1} {(dq_board[0][0] * 1)+(dq_board[1][0] * 2)+(dq_board[2][0] *4)+(dq_board[3][0]*8)}")