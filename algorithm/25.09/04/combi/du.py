T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    total_box = [0]*3
    z = n//2
    zzang = 0
    for a in range(len(total_box)):
        visited = [0] * (len(arr)+1)
        for i in arr:
            visited[i] += 1
            if visited[i] > n/2:
                print(-1)
                break
            else:
                for k in range(z):
                    total_box[k] += 1
    zzang = min(abs(total_box[1] - total_box[2]), abs(total_box[0]-total_box[1]),abs(total_box[0]-total_box[2]))
    print(f'#{test_case} {zzang}')