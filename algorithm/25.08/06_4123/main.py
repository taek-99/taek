T = int(input())

for tc in range (T):
    n = int(input())
    num = list(map(int, input().split()))
    card_list = list(map(int, input().split()))
    min_ans = 10 ** 10
    max_ans = -10 ** 10

    def dfs(index, calcus, result):
        global max_ans
        global min_ans

        if index == n-1:
            max_ans = max(result, max_ans)
            min_ans = min(result, min_ans)
            return

        if calcus[0]: #더하기
            next_calcus = calcus[:]
            next_calcus[0] -= 1
            dfs (index + 1, next_calcus, result + card_list[index +1])
        if calcus[1]: #빼기
            next_calcus = calcus[:]
            next_calcus[1] -= 1
            dfs (index + 1, next_calcus, result - card_list[index +1])
        if calcus[2]: # 곱하기
            next_calcus = calcus[:]
            next_calcus[2] -= 1
            dfs (index + 1, next_calcus, result * card_list[index +1])
        if calcus[3]: # 나누기
            next_calcus = calcus[:]
            next_calcus[3] -= 1
            dfs (index + 1, next_calcus, int(result / card_list[index + 1]))



    result = card_list[0]
    dfs (0, num, result) #현재 숫자위치, 연산카드, 결과값

    print (f"#{tc+1} {max_ans - min_ans}")