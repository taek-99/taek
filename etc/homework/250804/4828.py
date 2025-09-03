T = int(input())
 
for tc in range (T):
    n = int(input())
    num = list(map(int, input().split()))
    print (f"#{tc+1} {max(num) - min(num)}")