import sys
sys.stdin = open('taek/algorithm/25.08/26/sea25038/input1.txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    num = [list(map(int, input().split())) for _ in range(n)]

    child = [[] for _ in range(n+1)]
    for idx, row in enumerate(num, start=1):
        child[idx] = row[1:]

    ans_list = set()
    tt = 0

    while True:
        ready = []
        for i in range(1, n+1):
            if not child[i] and i not in ans_list:
                ready.append(i)
        
        if not ready:  # 작업 종료
            if len(ans_list) == n:
                print (f"#{tc} {tt}")
            else:
                print (f"#{tc} -1")
            break

        
        ans_list.update(ready)
        tt += 1

        ready_set = set(ready)
        for i in range(1, n+1):
            if child[i]:
                new_list = []
                for j in child[i]:
                    if j not in ready_set:
                        new_list.append(j)
                child[i] = new_list

