from itertools import permutations, combinations, product, combinations_with_replacement

""" 순열(permutation)
    서로 다른것 중 몇개를 뽑아서 순서대로 나열하는 것
    시간 복잡도: N! -> 
"""

print ("num 리스트를 순열로 +++++++++++++")
num = [1, 2, 3]
n = 3
# for 문 구현 버전
# 문제점은 n의 개수만큼 for문을 추가로 중첩해야하기 때문에
# n의 갯수가 고정값이 아니면 사실상 구현 불가
print ("for문 버전========")
for i in range(n):
    for j in range(n):
        if i != j:
            for k in range(n):
                if k != i and k != j:
                    print ([num[i], num[j], num[k]])

# 재귀 구현 버전
print ("재귀 버전========")
def perm(selected, remain):
    if not remain:  # remain이 비어있으면 selected를 출력
        print(selected)
    else:
        for i in range(len(remain)):
            selected_i = remain[i]    # remain에서 원소 하나 빼와서 selected_i에 넣음
            remain_list = remain[:i] + remain[i+1:]  # remain에서 뺀 원소를 제외한 남은 애들을 리스트로 저장
            perm(selected + [selected_i], remain_list)  # 재귀

perm([], num)

# itertools 사용
print ("딸깍 =======")
for val in permutations(num, n):
    print (list(val))


""" 조합(combinations)
    순서를 고려하지 않고 아이템을 선택하는 방법
    조합의 수식: nCr --> n개의 갯수를 r개로 만들수 있는 조합 
"""
print ()
print ("num 리스트를 조합으로 ++++++++++++")
num = [1,2,3,4]
n = 3
# for 문 구현 버전
# 문제점은 n개의 원소를 포함하는 조합을 만드는것이기 때문에
# n의 갯수만큼 for문 중첩해야함
print ("for문 버전========")
for i in range(4):
    for j in range(i+1, 4):
        for k in range(j+1, 4):
            print ([num[i], num[j], num[k]])

# 재귀 구현 버전
print ("재귀 버전========")
def comb(arr, n):
    result = []
    if n == 1:  
        return [[i] for i in arr]
    
    for i in range(len(arr)):
        elem = arr[i]
        for rest in comb(arr[i + 1:], n-1):
            result.append([elem]+rest)

    return result
    
print(comb(num, 3))

# itertools 사용
print ("딸깍 =======")
for idx in combinations(num, n):
    print (list(idx))


""" 부분 집합
    집합에 포함된 원소들을 선택하는 것
    각 원소를 부분집합에 포함하거나 포함하지 않는 2가지 경우를 모든 원소에 적용한것과 같다
    시간 복잡도: 2**n
"""
print ()
print ("num 리스트를 부분집합으로 ++++++++++++")
num = [1,2,3]
n = 3
selected = [0] * 3

# for 문 구현 버전
# 문제점은 n개의 원소를 포함하는 조합을 만드는것이기 때문에
# n의 갯수만큼 for문 중첩해야함
print ("for문 버전========")
for i in range(2):
    selected[0] = i
    for j in range(2):
        selected[1] = j
        for k in range(2):
            selected[2] = k
            subset = []
            for l in range(3):
                if selected[l] == 1:
                    subset.append(num[l])
            print (subset)
            # print (selected, subset) # 가독성 높인 버전

# 재귀 구현 버전
print ("재귀 버전========")

def generate_subset(idx, included):
    if idx == n:
        cnt_subset = []  # 교제랑 좀 다르게 짰는데 가독성 높이고 
        for i in range(n):  # 쉽게 생각해서 각 포인트가 True면 그 값을 리스트에 추가
            if included[i]:
                cnt_subset.append(num[i])
        subset.append(cnt_subset)
        return
    
    included[idx] = False
    generate_subset(idx +1, included)

    included[idx] = True
    generate_subset(idx +1, included)

subset = []
init_included = [False] * n
generate_subset(0, init_included)
print (subset)


# 바이너리 카운팅 버전 - 비트로 구현한것
# 정수를 이진수로 변환하는법을 알고 잇으면 편합니다.
# 이건 저도 헷갈려서 틀릴수도 있어여
print ("바이너리 카운팅 버전========")

subset_cnt = 2 ** n

ans_list = []
for i in range(subset_cnt):
    subset = []
    for j in range(n):
        if i & (1 << j):  # 여기를 이해하시면 되는데 2진수로 변환했을 때 
                          # 각 비트가 1이면 그자릿수를 subset 리스트에 포함시키는 거에요
            subset.append(num[j])
    ans_list.append(subset)

print (ans_list)


########### 여기서부턴 참고에 있던 것들이라 필수는 아닌듯 하여###########
########### 주석처리 해놨으니 필요한 사람들만 확인 #####################

# num = [1,2,3]
# n = 2
# """ 중복 순열(product)
#     순서를 고려하여 여러번 선택할 수 있게 나영하는 모든 가능한 방법
#     예) 비밀번호 생성시 같은 번호 여러번 사용하는 경우
# """
# print ()
# print ("num 리스트를 중복순열로 ++++++++++++")
# # itertools 사용
# print ("딸깍 =======")
# for idx in product(num, repeat=n):
#     print (list(idx))

# """ 중복 조합(product)
#     순서를 고려하지 않고 여러번 선택할 수 있게 나열하는 모든 가능한 방법
#     예) 아이스크림 원하는 맛으로 여러개 선택하는 경우
# """
# print ()
# print ("num 리스트를 중복조합으로 ++++++++++++")
# # itertools 사용
# print ("딸깍 =======")
# for idx in combinations_with_replacement(num, n):
#     print (list(idx))