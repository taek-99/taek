import sys
input = sys.stdin.readline

n = int(input())
man = list(map(int, input(). split()))
man.insert(0, 0)
ans_man = [0] * n

### 약 프로그램 3번 엎고 이것저것 찾아보면서 완료.

for i in range (1, n+1): # 제일 작은 사람부터 시작
    cnt = man[i]
    for j in range (n):
        if ans_man[j] == 0 :# 서야할 자리가 비어있는지 확인
            if cnt == 0: 
                ans_man[j] = i
                break
            cnt -= 1

print (*ans_man)