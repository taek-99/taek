import sys
sys.stdin = open('sample_input (24).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    a_list.sort()
    ans = 0

    for key in b_list:
        low = 0
        high = n - 1
        last_dir = 0
        while low <= high:
            mid = low + (high - low) // 2

            if a_list[mid] == key:
                ans += 1
                break
            elif a_list[mid] > key:
                high = mid - 1

                if last_dir == 1:
                    break
                last_dir = 1
            else:
                low = mid + 1

                if last_dir == -1:
                    break
                last_dir = -1

    print(f"#{tc} {ans}")