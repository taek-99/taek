## 16:22
## 16:28

import sys
sys.stdin = open('switch_sample_in.txt','r')


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if a_list[i] != b_list[i]:
            cnt +=1
            for j in range(i, n):
                if a_list[j] == 1:
                    a_list[j] = 0
                else:
                    a_list[j] = 1

    print (f"#{tc} {cnt}")
