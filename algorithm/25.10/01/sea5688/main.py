import sys
sys.stdin = open('sample_input (23).txt','r')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    val = 1

    ans = -1
    while True:
        if val ** 3 == n:
            ans = val
            break

        if val ** 3 > n:
            break

        val += 1

    print(f"#{tc} {ans}")