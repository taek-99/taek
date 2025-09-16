import sys
sys.stdin = open('sample_input (13).txt','r')

from collections import defaultdict

T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    bug_dict = {}
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    dir_change = [0, 2, 1, 4, 3]

    for i in range(k):
        x, y, cnt, d = map(int, input().split())
        bug_dict[i+1] = [(x, y), cnt, d]

    while m:
        for idx, val in bug_dict.items():  # 이동
            x = val[0][0]
            y = val[0][1]
            nx, ny = x + dx[val[2]], y + dy[val[2]]

            if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:  # 외곽에 닿음
                val[1] = val[1] // 2
                val[2] = dir_change[val[2]]

            val[0] = (nx, ny)

        by_pos = defaultdict(list)
        for idx, val in bug_dict.items():  # 같은 좌표에 두개 이상 있나 확인
            by_pos[(val[0][0], val[0][1])].append(idx)

        for pos, idx in by_pos.items():  # 여러 군집 있으면 삭제
            if len(pos) < 2:
                continue

            king = max(idx, key=lambda i: bug_dict[i][1])
            total_cnt = sum(bug_dict[i][1] for i in idx)

            bug_dict[king][1] = total_cnt

            for i in idx:
                if i != king:
                    del bug_dict[i]
        m -= 1

    ans = 0
    for val in bug_dict.values():
        ans += val[1]

    print(f"#{tc} {ans}")

