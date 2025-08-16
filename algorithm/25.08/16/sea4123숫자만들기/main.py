T = int(input())

for tc in range(1, T+1):
    n = int(input())
    n_list = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    
    min_num = 10 ** 10
    max_num = -10 ** 10

    def dfs(idx, cal, result):
        global min_num
        global max_num
    
        if idx == n-1:
            min_num = min(min_num, result)
            max_num = max(max_num, result)
            return
    
        if cal[0] > 0: # 더하기
            cal[0] -= 1
            dfs (idx+1, cal, result + nums[idx+1])
            cal[0] += 1
            
        if cal[1] > 0: # 빼기
            cal[1] -= 1
            dfs (idx+1, cal, result - nums[idx+1])
            cal[1] += 1
            
        if cal[2] > 0: # 곱하기
            cal[2] -= 1
            dfs (idx+1, cal, result * nums[idx+1])
            cal[2] += 1
            
        if cal[3] > 0: # 나누기
            cal[3] -= 1
            dfs (idx+1, cal, int(result / nums[idx+1]))
            cal[3] += 1
        
    dfs(0, n_list, nums[0])
    
    print (f"#{tc} {max_num-min_num}")