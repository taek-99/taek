import sys
sys.stdin = open('sample_input (28).txt','r')

from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    pos_list = set()
    for i in range(n):
        pos_list.add(i)

    min_ans = 10 ** 10
    for food_a_pos in combinations(range(n), n//2):
        food_b_pos = pos_list - set(food_a_pos)

        food_a = 0
        food_b = 0
        for idx in combinations(food_a_pos, 2):
            food_a += board[idx[0]][idx[1]] + board[idx[1]][idx[0]]

        for idx in combinations(food_b_pos, 2):
            food_b += board[idx[0]][idx[1]] + board[idx[1]][idx[0]]

        min_ans = min(min_ans, abs(food_a - food_b))

    print (f"#{tc} {min_ans}")