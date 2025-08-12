from collections import defaultdict

T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    bug_dict = {}
    
    for i in range(1, k+1):
        x, y, cnt, dir = map(int, input().split())
        bug_dict[i] = [(x, y), cnt, dir]
    
    
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    dir_change = [0, 2, 1, 4, 3]
    
    def sol_move(key, bug):
        x = bug[0][0]
        y = bug[0][1]
        cnt = bug[1]
        dir = bug[2]
        nx = x + dx[dir]
        ny = y + dy[dir]
    
        if not (0 < nx < n-1 and 0 < ny < n-1): #바깥라인 닿았을때
            bug_dict[key][2] = dir_change[dir]
            bug_dict[key][1] = cnt // 2
        bug_dict[key][0] = (nx, ny)

    
    def sol_meet():
        by_pos = defaultdict(list)
        for num, (pos, cnt, d) in bug_dict.items():
            by_pos[pos].append(num)
    
        for pos, ids in by_pos.items():
            if len(ids) <= 1:
                continue
                
            king = max(ids, key=lambda i: bug_dict[i][1])
    
            total_cnt = sum(bug_dict[i][1] for i in ids)
            bug_dict[king][1] = total_cnt
    
            for i in ids:
                if i != king:
                    del bug_dict[i]
    
    for i in range(m):
        for i, v in bug_dict.items():
            sol_move(i, v)
        sol_meet()
    
    ans_sum = 0
    for i in bug_dict:
        ans_sum += bug_dict[i][1]
    
    print (f"#{tc} {ans_sum}")