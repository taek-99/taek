T = int(input())

for t in range (T):
    k, n, m = map(int, input().split())
    charge = list(map(int, input(). split()))
    arr = [0] * n
    
    # 충전소 위치 길에 입력
    for i in charge:
        arr[i-1] = i
    arr.insert(0, 0)
    
    aaa = 0
    cnt = 0
        
    
    while aaa != n:
        a = 0
        b = False # 충전소 찾았는지 확인
        
        # 현재 위치부터 갈수 있는 위치 안에 충전기 확인
        for i in range (aaa+1, aaa+k+1):
            # 가장 오른쪽에 있는 충전소 위치 저장
            if arr[i] > 0:
                a = i
                b = True
            if i == n:
                a = i
                break
                
        #종착역에 다다름
        if a == n:
            break
    
        # 충전소 찾았을 경우 현 위치를 최대한 오른쪽의 충전기 위치로 바꾸고 초기화 +카운팅까지
        if b == True:
            cnt += 1
            aaa = a
        # 충전소를 못 찾았을 경우 탈출하고 cnt 초기화
        else:
            cnt = 0
            break
                    
    print (f"#{t+1} {cnt}")
                