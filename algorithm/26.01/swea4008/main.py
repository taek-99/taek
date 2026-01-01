import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    nums = list(map(int, input().split()))


    def dfs(ans, idx):
        global max_num, min_num

        if idx == N:  # 마지막
            max_num = max(max_num, ans)
            min_num = min(min_num, ans)
            return

        if arr[0] > 0:  # 덧셈
            arr[0] -= 1
            dfs(ans + nums[idx], idx + 1)
            arr[0] += 1

        if arr[1] > 0:  # 뺄셈
            arr[1] -= 1
            dfs(ans - nums[idx], idx + 1)
            arr[1] += 1

        if arr[2] > 0:  # 곱셈
            arr[2] -= 1
            dfs(ans * nums[idx], idx + 1)
            arr[2] += 1

        if arr[3] > 0:  # 나눗셈
            arr[3] -= 1
            dfs(int(ans / nums[idx]), idx + 1)
            arr[3] += 1

        return


    max_num = -10**10
    min_num = 10**10
    dfs(nums[0], 1)

    print(f"#{tc} {max_num - min_num}")




  
