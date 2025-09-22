import sys
sys.stdin = open('sample_input (16).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    cell_dict = {}
    for i in range(1, n+1):
        x, y, d, k = map(int, input().split())
        x *= 2
        y *= 2
        cell_dict[i] = [x, y, d, k]

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]


    ans = 0
    while True:
        del_dict = []
        for key, val in cell_dict.items():  # 이동
            val[0] += dx[val[2]]
            val[1] += dy[val[2]]

            if abs(val[0]) > 2000 or abs(val[1]) > 2000:
                del_dict.append(key)

        if del_dict:  # 범위 벗어나면 삭제
            for i in list(cell_dict.keys()):
                if i in del_dict:
                    del cell_dict[i]

        dup_list = set()
        seen = set()
        for i in cell_dict:  # 겹치는거 있나 확인
            x = cell_dict[i][0]
            y = cell_dict[i][1]
            if (x, y) in seen:
                dup_list.add((x, y))
            else:
                seen.add((x, y))

        if dup_list:  # 만나는 원소 삭제 & 정답에 더해주기
            crash_ids = set()
            for i in reversed((list(cell_dict))):
                x = cell_dict[i][0]
                y = cell_dict[i][1]
                if (x, y) in dup_list:
                    ans += cell_dict[i][3]
                    del cell_dict[i]

        if len(cell_dict) < 2:
            break

    print(f"#{tc} {ans}")