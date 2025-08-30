import sys
sys.stdin = open('25.08/30/sea2382/sample_input (37).txt','r')


from collections import defaultdict

T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    bug_dict = {}
    for i in range(1, k+1):
        row, col, num, dir = map(int, input().split())
        bug_dict[i] = [row, col, num, dir]

    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    dir_change = [0, 2, 1, 4, 3]

    while m:
        cnt_list = [[] for _ in range(len(bug_dict))]
        dir_list = [[] for _ in range(len(bug_dict))]
        set_list = set()
        for idx, val in bug_dict.items():
            row = val[0]
            col = val[1]
            cnt = val[2]
            dir = val[3]

            nx = row + dx[dir]
            ny = col + dy[dir]
            if 0 == nx or n-1 == nx or 0 == ny or n-1 == ny:
                val[2] = cnt // 2
                val[3] = dir_change[dir]
            
            val[0] = nx
            val[1] = ny
        
        by_pos = defaultdict(list)
        for num, val in bug_dict.items():
            by_pos[(val[0], val[1])].append(num)
        
        for pos, idx in by_pos.items():
            if len(idx) <= 1:
                continue
                
            king = max(idx, key=lambda i: bug_dict[i][2])
            total_cnt = sum(bug_dict[i][2] for i in idx)

            bug_dict[king][2] = total_cnt

            for i in idx:
                if i != king:
                    del bug_dict[i]

        m -= 1

        ans_sum = 0
        for idx in bug_dict:
            ans_sum += bug_dict[idx][2]
        
    print (f"#{tc} {ans_sum}")