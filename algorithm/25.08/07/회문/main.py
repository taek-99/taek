import sys
sys.stdin = open("sample_input (16).txt", "r")

T = int(input())

for tc in range (1, T+1):
    n, m = map(int, input().split())
    word_list = []
    for _ in range (n):
        word_list.append(input())

    ans_word = ""
    for i in range (n): #가로 확인
        wid_word = ""
        for j in range (0, n-m+1):
            wid_word = word_list[i][j:j+m]
            if wid_word == wid_word[::-1]:
                ans_word = wid_word
                break
        if ans_word:
            break

    if not ans_word: #세로 확인
        for i in range (n):
            for j in range(0, n-m+1):
                len_word = ""
                for k in range (j, j+m):
                    len_word += word_list[k][i]
                if len_word == len_word[::-1]:
                    ans_word = len_word
                    break
            if ans_word:
                break

    print (f"#{tc} {ans_word}")