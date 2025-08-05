n, l = map(int, input().split())

for i in range (l, 101):
    # 수열 구하기 위한 공식
    # (n - (x+(x+1)+(x+2)+ .....)) // l
    num = (n - (i * (i - 1) // 2)) / i

    # 시작값이 음수면 안되고 앞으로 더 해봤자 값은 더작아지기 때문에 의미 없음
    if num < 0:
        print (-1)
        break

    #num이 정수이고 0보다 커야함
    if num.is_integer() and num >= 0 :
        sn = int(num) 
        print(*range(sn, sn + i))
        break
else:
    print(-1)