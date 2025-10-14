
T = int(input())  # 테케

N, L = map(int ,input().split())
ham_list = [list(map(int, input().split())) for _ in range(N)]


def dfs(idx, score, cal):
    global max_score

    if cal > L:  # 현재 칼로리가 최대 칼로리 넘으면 더할필요가 없음 ㅇㅋ? 그래서 그냥 return 으로 하는거에여
        return

    max_score = max(max_score, score)

    if idx == N:  ## 인덱스 번호가 N이 되면 종료
        return

    dfs(idx+1, score + ham_list[idx][0], cal + ham_list[idx][1])
    dfs(idx+1, score, cal)


max_score = 0
dfs (0, 0, 0)

print (max_score)