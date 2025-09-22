import sys
sys.stdin = open('sample_input (16).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    str_list = []
    for _ in range(n):
        str_list.append(input().strip())

    ans_list = ""


    def dfs(idx, ans):
        global cnt

        if len(set(ans)) == 26:
            cnt += 1 << (n - idx)
            return

        if idx == n:
            return

        dfs(idx + 1, ans)
        dfs(idx + 1, ans + str_list[idx])


    cnt = 0
    dfs(0, ans_list)
    print(f"#{tc} {cnt}")