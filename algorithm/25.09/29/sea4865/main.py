import sys
sys.stdin = open('sample_input (21).txt','r')

T = int(input())

for tc in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    max_cnt = 0
    for val in str1:
        cnt = 0
        for val2 in str2:
            if val == val2:
                cnt += 1
        max_cnt = max(max_cnt, cnt)

    print(f"#{tc} {max_cnt}")