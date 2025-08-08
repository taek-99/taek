from collections import deque
import sys
sys.stdin = open('sample_input (19).txt','r')

T = int(input())

for tc in range (1, T+1):
    str_list = input()
    par_list = {'{' : '}', '(' : ')', '}' : '{', ')' : '('}
    ans_list = []
    ans = 1

    for i in str_list:
        if i in par_list:
            if not ans_list or ans_list[-1] != par_list[i]:
                ans_list.append(i)
            elif ans_list[-1] == par_list[i]:
                del ans_list[-1]

    if ans_list:
        ans = 0

    print (f"#{tc} {ans}")