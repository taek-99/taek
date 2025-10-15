import json

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    nums = json.loads(input().strip())


    def dfs(dept, arr):
        global ans
        
        dept += 1  # 깊이 추가
        for val in arr:
            if isinstance(val, int):  # 정수인지 확인
                ans += val * dept
            else:
                dfs(dept, val)


    ans = 0
    dfs(0, nums)  # 깊이 확인용, 리스트

    print (f"#{tc} {ans}")