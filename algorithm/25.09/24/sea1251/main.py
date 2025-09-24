import sys
sys.stdin = open('re_sample_input.txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    x_pos = list(map(int, input().split()))
    y_pos = list(map(int, input().split()))
    e = float(input())
    node = list(zip(x_pos, y_pos))
    visited = set()

    start_num = 0
    visited.add(0)
    x, y = node[0]
    ans = 0

    mindist = [float("INF")] * n
    mindist[0] = 0

    while True:

        for i, (nx, ny) in enumerate(node):
            if i in visited:
                continue

            dx = x - nx
            dy = y - ny
            mindist[i] = min(mindist[i], (dx * dx + dy * dy))

        min_pos = float('INF')
        next_pos = -1

        for i in range(n):
            if i in visited:
                continue
            if mindist[i] < min_pos:
                min_pos = mindist[i]
                next_pos = i

        if next_pos != -1:  # 사실상 모든 visited방문했다는 뜻
            ans += min_pos
            x, y = node[next_pos]
            visited.add(next_pos)
        else:
            break

    print(f"#{tc} {round(ans * e)}")


