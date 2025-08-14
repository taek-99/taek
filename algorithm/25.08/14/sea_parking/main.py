import sys
sys.stdin = open('sample_input (26).txt','r')
from collections import deque

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())

    price_list = []
    car_list = []
    for i in range(n):
        price_list.append(int(input()))
    for i in range(m):
        car_list.append(int(input()))
    car_list.insert(0, 0)


    parking_list = [0] * n
    wait_list = deque([])
    money = 0
    for _ in range(m*2):
        i = int(input())

        if i > 0:
            wait_list.append(i) # 일단 대기
            for j in range(n):
                if parking_list[j] == 0:
                    car_num = wait_list.popleft()
                    parking_list[j] = car_num
                    money += price_list[j] * car_list[car_num]
                    break
        else: # 출차 과정
            for j in range(n):
                if parking_list[j] == abs(i):
                    parking_list[j] = 0
                    if wait_list: # 출차하고 나서 대기 차량이 있을때
                        car_num = wait_list.popleft()
                        parking_list[j] = car_num
                        money += price_list[j] * car_list[car_num]
                    break

    print (f"#{tc} {money}")