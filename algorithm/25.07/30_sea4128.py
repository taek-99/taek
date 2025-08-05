from itertools import combinations

# 콤비네이션 안쓰고 싶어서 고집부리다 1시간 넘게 버린 사실....

# 입력
T = int(input())
for tc in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range (N)]
    sum_list = set([i for i in range (N)] )
    ans = 1000000
    
    for food_a_pos in combinations(range(N), (N//2)):
        food_b_pos = sum_list - set(food_a_pos)
    
        food_a = food_b = 0
        # a음식 맛
        for i in food_a_pos:
            for j in food_a_pos:
                if i != j:
                    food_a += board[i][j]
        # b음식 맛
        for i in food_b_pos:
            for j in food_b_pos:
                if i != j:
                    food_b += board[i][j]
        
        ans = min(ans, abs(food_a - food_b))
        if ans == 0:
            break
    print (f"#{tc+1} {ans}")