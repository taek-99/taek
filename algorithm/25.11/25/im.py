
## 이해하기 쉬운 버전 ## 
T = int(input())
for tc in range(1, T+1):
    n, w1, w2 = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    top1 = []
    top2 = []

    for idx in range(1, n+1):  # 각 탑에 높이 도달하기 전까지 탑 쌓기
        if len(top1) < w1:
            x1 = arr.pop()
            top1.append(x1)
        
        if len(top2) < w2:
            x2 = arr.pop()
            top2.append(x2)
    

    ans = 0
    for idx in range(n): # 각 층에 물건이 있으면 층*물건 무게 해서 ans에 더하기
        floor = idx + 1

        if len(top1) > idx:
            ans += floor * top1[idx]
        if len(top2) > idx:
            ans += floor * top2[idx]

    print(f"#{tc} {ans}")



## 효율 높인 버전 ##
T = int(input())

for tc in range(1, T+1):
    n, w1, w2 = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    
    for idx in range(1, n+1):
        if w1 > 0:
            ans += (idx*arr.pop())
            w1 -= 1
        
        if w2 > 0:
            ans += (idx*arr.pop())
            w2 -= 1
        
    print(f"#{tc} {ans}")