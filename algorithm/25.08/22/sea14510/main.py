import sys
sys.stdin = open('Sample_input (8).txt','r')

# T = int(input())
#
# for tc in range(1, T+1):
#     n = int(input())
#     trees = list(map(int, input().split()))
#
#     max_tree = max(trees)
#     tree_list = [max_tree - val for val in trees]
#
#     odd_need = 0
#     even_need = 0
#     for tt in trees:
#         d = max_tree - tt
#         odd_need += d % 2
#         even_need += d // 2
#
#     if odd_need == 0 and even_need == 0:
#         ans = 0
#
#
#     def dfs(o, e, start_odd = True):
#         days = 0
#         is_odd_day = start_odd
#         while o > 0 or e > 0:
#             days += 1
#             if is_odd_day:
#                 if o > 0:
#                     o -= 1
#                 elif e > 0:
#                     e -= 1
#                     o += 1
#             else:
#                 if e > 0:
#                     e -= 1
#
#             is_odd_day = not is_odd_day
#         return days
#
#
#     if not ans:
#         ans1 = dfs(odd_need, even_need, start_odd = True)
#         ans2 = dfs(odd_need, even_need, start_odd = False) + 1
#         print(f"#{tc} {min(ans1, ans2)}")
#     else:
#         print ("#{tc} 0")

T = int(input().strip())
for tc in range(1, T+1):
    n = int(input().strip())
    h = list(map(int, input().split()))
    M = max(h)
    diffs = [M - x for x in h]

    S = sum(diffs)  # 총 필요량
    A = sum(d & 1 for d in diffs)  # 홀수 필요량 개수

    # 짝수 m 후보: m = 2k, k >= max(A, ceil(S/3))

    k_even = max(A, (S + 2) // 3)  # ceil(S/3) = (S+2)//3
    m_even = 2 * k_even

    # 홀수 m 후보: m = 2k+1, k >= max(A-1, ceil((S-1)/3))
    k_odd = max(max(0, A - 1), (S + 1) // 3)  # ceil((S-1)/3) = (S+1)//3
    m_odd = 2 * k_odd + 1

    print(f"#{tc} {min(m_even, m_odd)}")
