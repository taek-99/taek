import sys
sys.stdin = open('sample_input (28).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]


    def ascent(x, data):
        for j in range(x, x-k, -1):
            if j < 0 or bd[j] != data or used[j]:
                return False

        for j in range(x, x - k, -1):
            used[j] = True
        return True


    def down_hil(x, data):
        for j in range(x+1, x+k+1):
            if j >= n or bd[j] != data or used[j]:
                return False

        for j in range(x + 1, x + k + 1):
            used[j] = True
        return True


    def sol(line):
        for i in range(n - 1):
            diff = line[i+1] - line[i]
            if diff == 0:
                continue

            if diff == 1: # 오르막
                if not ascent(i, line[i]):
                    return False
            elif diff == -1: # 내리막
                if not down_hil(i, line[i + 1]):
                    return False
            else:
                return False
        return True

    cnt = 0
    for bd in board: # 행 확인
        used = [False] * n
        if sol (bd):
            cnt += 1

    for bd in zip(*board): # 열 확인
        used = [False] * n
        if sol (list(bd)):
            cnt += 1

    print (f"#{tc} {cnt}")