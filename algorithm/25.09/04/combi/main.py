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
    b_box = []
    m_box = []
    s_box = []
    bad_car = n // 2

    for i in range(nn//3+1):
        s_box.append(carrot[i])
        if sum(s_box) > bad_car:
            break
        m_box = []
        for j in range(i+1, i+nn//3+1):
            m_box.append(carrot[j])
            if sum(m_box) > bad_car:
                break   
            b_box = []
            for k in range(j+1, j+nn//3+1):
                b_box.append(carrot[k])
                if sum(b_box) > bad_car:
                    break

            if not s_box:
                break
            if not m_box:
                break
            if not b_box:
                break
            
            print (s_box, m_box, b_box)
            if len(s_box+m_box+b_box) == nn:
                a = sum(s_box)
                b = sum(m_box)
                c = sum(b_box)
                ans = min(abs(a-b), abs(a-c), abs(b-c))

    print (f"#{tc} {ans}")



