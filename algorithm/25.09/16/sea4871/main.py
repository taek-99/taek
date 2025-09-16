import sys
sys.stdin = open('sample_input (13).txt','r')

T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())
    child = [[] for _ in range(v+1)]

    for _ in range(e):
        x, y = map(int, input().split())
        child[x].append(y)

    sp, ep = map(int, input().split())


    def dfs(pos):
        global complete

        if pos == ep:
            complete = 1

        if complete:
            return

        for idx in child[pos]:
            dfs(idx)


    complete = 0
    dfs(sp)

    print(f"#{tc} {complete}")