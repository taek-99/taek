import sys
sys.stdin = open('input.txt','r')

from collections import deque

n = int(input())
people = list(map(int, input().split()))
parents = [[] for _ in range(n+1)]

for j in range(n):
    nums = list(map(int, input().split()))
    for i in range(1, len(nums)):
        parents[j+1].append(nums[i])


def sol(team):  # 이어져있는지 확인
    if len(team) == 1:
        return True

    okay = False
    q = deque()
    seen = set()
    q.append(team[0])
    seen.add(team[0])

    while q:
        x = q.popleft()
        for nx in parents[x]:
            if nx in team and nx not in seen:
                seen.add(nx)
                q.append(nx)

    return len(seen) == len(team)


def men_plus(team):  # 인원수 합
    sum_men = 0
    for idx in team:
        sum_men += people[idx-1]
    return sum_men


min_num = 10 ** 10
for i in range(1, 2**n-1):
    a_team = []
    b_team = []
    for j in range(n):
        if (i >> j) & 1 == 1:
            a_team.append(j+1)
        else:
            b_team.append(j+1)

    if not sol(a_team) or not sol(b_team):  # 둘 중 한팀이라도 연결 안되어 있으면
        continue

    min_num = min(min_num, abs(men_plus(a_team) - men_plus(b_team)))

    if min_num == 0:
        break

if min_num == 10**10:
    print(-1)
else:
    print(min_num)