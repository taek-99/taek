from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    pizza_list = deque(map(int, input().split()))
    fire_pit = deque([(0, 0)] * n)

    idx = 1
    while pizza_list:
        if fire_pit[-1][0] == 0:
            fire_pit[-1] = (pizza_list.popleft(), idx)
            idx += 1
        else:
            fire_pit[-1] = (fire_pit[-1][0] // 2, fire_pit[-1][1])
            if fire_pit[-1][0] == 0:
                fire_pit[-1] = (pizza_list.popleft(), idx)
                idx += 1
        fire_pit.rotate(1)

    while True:
        fire_pit[-1] = (fire_pit[-1][0] // 2, fire_pit[-1][1])
        if fire_pit[-1][0] == 0:
            del fire_pit[-1]
        else:
            fire_pit.rotate(1)

        if len(fire_pit) == 1:
            print(f"#{tc} {fire_pit[0][1]}")
            break