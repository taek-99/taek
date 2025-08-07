import sys
sys.stdin = open('s_input (1).txt', 'r')

T = int(input())

for tc in range (T):
    n = int(input())
    bus_list = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())

    num_list = [0] * 5001
    p_list = []
    for i in range(p):
        a = int(input())
        p_list.append(a-1)

    for i in bus_list:
        for j in range(i[0], i[1]+1):
            num_list[j-1] += 1

    ans_list = []
    for i in p_list:
        ans_list.append(num_list[i])

    ans = " ".join(map(str, ans_list))
    print (f"#{tc+1} {ans}")
