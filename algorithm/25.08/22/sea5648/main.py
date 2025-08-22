import sys
sys.stdin = open('sample_input (7).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    atom_list = {}

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(1, n+1):
        atom_list[i] = list(map(int, input().split()))
        atom_list[i][0] *= 2
        atom_list[i][1] *= 2

    ans = 0
    while True:
        del_list = set()
        for i in atom_list:
            d = atom_list[i][2]
            x = atom_list[i][1] + dx[d]
            y = atom_list[i][0] + dy[d]
            if -2001 < x < 2001 and -2001 < y < 2001:
                atom_list[i][1] = x
                atom_list[i][0] = y
            else:
                del_list.add(i)

        if del_list: # 범위 벗어나면 삭제
            for i in del_list:
                del atom_list[i]

        dup_list = set()
        seen = set()
        for i in atom_list:  # 겹치는거 있나 확인
            x = atom_list[i][0]
            y = atom_list[i][1]
            if (x, y) in seen:
                dup_list.add((x, y))
            else:
                seen.add((x, y))

        if dup_list:  # 만나는 원소 삭제 & 정답에 더해주기
            crash_ids = set()
            for i in reversed((list(atom_list))):
                x = atom_list[i][0]
                y = atom_list[i][1]
                if (x, y) in dup_list:
                    ans += atom_list[i][3]
                    del atom_list[i]

        if len(atom_list) < 2:  # 원자가 2개 미만으로 나오면 탈출
            break

    print(f"#{tc} {ans}")