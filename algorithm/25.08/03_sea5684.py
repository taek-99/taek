T = int(input())

# key point: 0.5초도 계산해야되기 때문에 기존 좌표의 * 2
# key point: 2000*2000이라는 임시의 판을 벗어나면 원자끼리 만날일 없음

for tc in range(T):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range (N)]
    
    atom_list = []
    for i in num:
        atom_list.append([i[0]*2, i[1]*2, i[2], i[3]])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    ans = 0
    tt = 0
    while True:
        tt +=1
        # 원자들 이동
        for i in range(len(atom_list)):
            atom_list[i][1] += dx[atom_list[i][2]]
            atom_list[i][0] += dy[atom_list[i][2]]
    
        # 좌표값 중복되면 삭제 리스트에 추가
        del_list = set()
        pre_list = set()
        for i in range(len(atom_list)):
            x, y = atom_list[i][0], atom_list[i][1]
            if (x, y) in pre_list:
                del_list.add((x, y))
            else:
                pre_list.add((x, y))
                
            
        for i in range(len(atom_list)-1, -1, -1):
            x, y = atom_list[i][0], atom_list[i][1]
            if (x, y) in del_list:
                ans += atom_list[i][3]
                atom_list.pop(i)
            elif max(abs(atom_list[i][0]), abs(atom_list[i][1])) > 2000:
                atom_list.pop(i)
       
        if len(atom_list) < 2:
            break
    
    print (f"#{tc+1} {ans}")