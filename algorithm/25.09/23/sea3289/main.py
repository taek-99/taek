import sys
sys.stdin = open('sample_input (17).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    p = list(range(n+1))
    rank = [0] * (n+1)


    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])
        return p[x]


    def union(x, y):
        px = find_set(x)
        py = find_set(y)

        if px != py:
            if rank[px] > rank[py]:
                p[py] = px
            elif rank[px] < rank[py]:
                p[px] = py
            else:
                p[py] = px
                rank[px] += 1

    ans = []
    for _ in range(m):
        k, x, y = map(int, input().split())

        if k == 0:
            union(x, y)

        if k == 1:
            if find_set(x) == find_set(y):
                ans.append('1')
            else:
                ans.append('0')

    print(f"#{tc} {''.join(ans)}")