import sys
sys.stdin = open('taek/algorithm/25.09/28/sea7465/s_input.txt','r')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    p_list = list(range(n+1))
    rank_list = [0] * (n+1)


    def find_set(x):
        if x != p_list[x]:
            p_list[x] = find_set(p_list[x])
        return p_list[x]


    def union_set (x, y):
        px = find_set(x)
        py = find_set(y)

        if px > py:
            p_list[px] = py
        else:
            p_list[py] = px


    for _ in range(m):
        x, y = map(int, input().split())
        union_set(x, y)

    for i in range(1, n+1):
        find_set(i)

    print(f"#{tc} {len(set(p_list))-1}")