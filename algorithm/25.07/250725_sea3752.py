from collections import deque

t = int(input())

for tc in range (t):
    n = int(input())
    
    num = deque(map(int, input(). split()))
    board = [0]

    ans = 0

    while num:
        dq = num.popleft()

        board.append(dq)
        
        for i in range (len(board)-1):
            board.append(dq+board[i])

                
        board = list(set(board))
 
    print (f"#{tc+1} {len(board)}")
            