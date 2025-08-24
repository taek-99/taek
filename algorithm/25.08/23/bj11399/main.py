T = int(input())
nums = list(map(int, input().split()))


nums.sort()

ans = 0
a = 0
for x in nums:
    a += x
    ans += a

print (ans)