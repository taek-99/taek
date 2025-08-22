import sys
sys.stdin = open('input (1).txt','r')

T = int(input())

for tc in range(1, T+1):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    for i in range(n):
        if i + 1 > nums[i] // m * k:
            print (f"#{tc} Impossible")
            break
    else:
        print(f"#{tc} Possible")