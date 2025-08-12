import sys
sys.stdin = open('sample_input (24).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    arr = input()
    cnt = []
    stick = []

    for i in arr:
        stick.append(i)

        if len(stick) >= 2:
            if stick[-2] == "(" and stick[-1] == ")":
                stick.pop()
                stick.pop()
                stick.append("a")

    ans = 0
    open_cnt = 0
    for i in stick:
        if i == "(":
            open_cnt += 1
        elif i =="a":
            ans += open_cnt
        else:
            open_cnt -= 1
            ans += 1


    print (f"#{tc} {ans}")
