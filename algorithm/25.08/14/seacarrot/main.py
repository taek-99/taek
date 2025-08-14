import sys
sys.stdin = open('carrot_sample_in.txt', 'r')


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    num_list = list(map(int, input().split()))


    max_cnt = 0
    for i in range(n):
        cnt = 1
        max_num = num_list[i]
        for j in range(i+1, n):
            if max_num < num_list[j]:
                cnt += 1
                max_num = num_list[j]
            else:
                break
        if cnt >= max_cnt:
            max_cnt = cnt

    print (f"#{tc} {max_cnt}")