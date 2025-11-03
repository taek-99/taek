
n = int(input())
arr = list(map(int, input().split()))
city = list(map(int, input().split()))

tt = 0
ans = 0
while tt < n-1:
    num = 0
    for i in range(tt+1, n):
        num += arr[i-1]
        if city[i] <= city[tt] or i == n-1:
            ans += city[tt] * num
            tt = i
            break


print(ans)