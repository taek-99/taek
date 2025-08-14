import sys
sys.stdin = open('input (23).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [[] for _ in range(n)]
    for i in range(n):
        board[i] = list(map(str, input().split()))


    ans_list = ""
    for i, v in board:
        for _ in range(int(v)):
            ans_list += i

    k = len(ans_list)

    print (f"#{tc}")
    for i in range(k):
        print(ans_list[i], end="")

        if i % 10 == 9:
            print ()
    print ()