# 16:12
# 16:35

from collections import deque

T = int(input())

for tc in range(1, T+1):
    k = int(input())
    board = [deque(map(int, input().split())) for _ in range(4)]
    nums = [list(map(int, input().split())) for _ in range(k)]
    
    for ma, v in nums:
        magnet_rotate = []
        magnet_rotate.append((ma-1, v))
        
        vv = v
        for i in range(ma-1+1, 4, 1): #오른쪽 확인
            vv *= -1
            if board[i][6] != board[i-1][2]:
                magnet_rotate.append((i, vv))
            else:
                break
    
        vv = v
        for i in range(ma-1-1, -1, -1): #왼쪽 확인
            vv *= -1
            if board[i][2] != board[i+1][6]:
                magnet_rotate.append((i, vv))
            else:
                break
                
        for i, vv in magnet_rotate:
            board[i].rotate(vv)
    
    print (f"#{tc} {board[0][0] + (board[1][0] * 2) + (board[2][0] * 4) + (board[3][0] * 8)}")
