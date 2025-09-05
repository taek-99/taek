import sys
sys.stdin = open('taek/algorithm/25.09/04/combi/sample_in (1).txt','r')


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    nums.sort()
    carrot = [0]

    a = nums[0]
    b = 0
    for i in range(n):
        if a == nums[i]:
            carrot[-1] += 1
        else:
            carrot.append(1)
            a = nums[i]
            
    ans = -1
    nn = len(carrot)
    m_box = []
    s_box = []
    bad_car = n // 2

    for i in range(nn):  # 작은 바구니
        s_box.append(carrot[i])
        if sum(s_box) > bad_car:
            break
        m_box = []
        for j in range(i+1, nn):  # 중간 바구니
            m_box.append(carrot[j])
            if sum(m_box) > bad_car:
                break   
            
            a = sum(s_box)
            b = sum(m_box)
            c = sum(carrot[j+1:]) # 큰 바구니
            
            if a == 0 or b == 0 or c == 0 or c > bad_car:  # 비어있는 상자가 있으면 pass
                continue    
 
            aaa = max(a, b, c) - min(a, b, c)
            if ans == -1:
                ans = aaa
            else:
                ans = min(ans, aaa)

    print (f"#{tc} {ans}")



