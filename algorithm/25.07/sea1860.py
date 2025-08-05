test_case = int(input())

for jj in range (test_case):
    n, m, k = map(int, input(). split())
    person = sorted(list(map(int, input(). split()))) #사람 오는 시간 오름차순
    
    ans = "Possible" #시작 값은 성공 세
    
    for i in range(n):
            if i + 1 > person[i] // m * k: #손님이 온 순서 > 손님이 오는 초//붕어빵 만드는 시간 * 붕어빵 갯수
            ans = "Impossible"
            break
        
    print (f"#{jj+1} {ans}")