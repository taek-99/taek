import sys
input = sys.stdin.readline

n = int(input())
rooms = [list(map(int, input().split())) for _ in range(n)]
room = sorted(rooms, key = lambda x: (x[1], x[0]))

end_time = -1
ans = 0

for st, et in room:
    if st >= end_time:
        end_time = et
        ans += 1 

print (ans)