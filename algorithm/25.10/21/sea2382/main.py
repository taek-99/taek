from collections import defaultdict

import sys
sys.stdin = open('taek/algorithm/25.10/21/sea2382/sample_input (41).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())

    bug_dict = defaultdict(list)
    for i in range(k):
        x, y, cnt, d = map(int, input().split())
        bug_dict[i] = [x, y, cnt, d]

    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    dxy_change = [0, 2, 1, 4, 3]

    while m:
        for idx, val in bug_dict.items():
            x, y, cnt, d = val

            nx = x + dx[d]  # 좌표 이동
            ny = y + dy[d]
            val[0] = nx
            val[1] = ny

            if 0 == nx or n-1 == nx or 0 == ny or n-1 == ny:  # 벽면에 닿았을때 동작
                val[3] = dxy_change[d]  # 방향전환
                val[2] = cnt // 2  # 반갈죽


        visited = defaultdict(list)
        for idx, val in bug_dict.items():
            x, y = val[0], val[1]
            visited[(x, y)].append((idx))

        for idx, val in visited.items():
            if len(val) >= 2:
                king_pos = 0
                max_cnt = 0
                for i in val:
                    if max_cnt < bug_dict[i][2]:
                        king_pos = i
                        max_cnt = bug_dict[i][2]

                for i in val:
                    if i != king_pos:
                        bug_dict[king_pos][2] += bug_dict[i][2]
                        del bug_dict[i]
                    
        m -= 1

    ans = 0
    for idx, val in bug_dict.items():
        ans += val[2]

    print (f"#{tc} {ans}")