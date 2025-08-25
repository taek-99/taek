import sys
sys.stdin = open('sample_input (32).txt','r')


T, score = map(int, input().split())
nn = int(input())
n, m, k = map(int, input().split())

star_list = []
for i in range(nn):  # 2진수 변환 후 리스트에 저장
    a = int(input())
    s = bin(a)[2:]
    s = s.zfill(25)
    star_list.append(s)

print (star_list)


