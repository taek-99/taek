
## 이건 시간 초과 버전
# #로컬에서 테스트 시
# #solution.py와 main.py 파일을 구분해 주세요.
# #main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.

# #제출 시 solution.py 부분만 변경하여 제출해 주세요.

# #####solution.py
# class RESULT:
#     def __init__(self, cnt, IDs):
#         self.cnt = cnt
#         self.IDs = IDs  # [int] * 5


# market_list = [[[[] for _ in range(120)] for _ in range(5)] for _ in range(5)] 
# discount_list = [[0 for _ in range(5)] for _ in range(5)] 
# id_list = [[[] for _ in range(5)] for _ in range(5)] 


# def init():
#     global market_list, discount_list, id_list

#     market_list = [[[{} for _ in range(120)] for _ in range(5)] for _ in range(5)] 
#     discount_list = [[0 for _ in range(5)] for _ in range(5)] 
#     id_list = [[[] for _ in range(5)] for _ in range(5)] 


# def sell(mID, mCategory, mCompany, mPrice):
#     global market_list, discount_list, id_list
    
#     bucket_idx = mPrice // 10000
#     mca = mCategory - 1
#     mco = mCompany - 1
#     price = mPrice + discount_list[mca][mco]

#     market_list[mca][mco][bucket_idx][mID] = [mca, mco, price]
#     id_list[mca][mco].append(mID)

#     total = 0
#     for i in range(120):
#         total += len(market_list[mca][mco][i])

#     return total

# def closeSale(mID):
#     global market_list, discount_list, id_list

#     for mca in range(5):
#         for mco in range(5):
#             for idx in range(120):
#                 if market_list[mca][mco][idx]:
#                     for num, val in market_list[mca][mco][idx].items():
#                         if num == mID:
#                             if val[2] - discount_list[mca][mco] > 0:
#                                 del market_list[mca][mco][idx][num]
#                                 return val[2] - discount_list[mca][mco]
#                             else:
#                                 return -1
#     return -1

# def discount(mCategory, mCompany, mAmount):
#     global market_list, discount_list, id_list
    
#     mca = mCategory - 1
#     mco = mCompany - 1
#     amount = discount_list[mca][mco] + mAmount
#     discount_list[mca][mco] = amount

#     alive = 0
#     for idx in range(120):
#         bucket = market_list[mca][mco][idx]
#         if not bucket:
#             continue

#         del_keys = []
#         for mid, val in bucket.items():
#             if val[2] <= amount:         
#                 del_keys.append(mid)

#         for k in del_keys:
#             bucket.pop(k, None)

#         # 남은 수 누적
#         alive += len(bucket)

#     return alive

# def show(mHow, mCode):

#     import heapq
#     global market_list, discount_list

#     if mHow == 0:
#         ca_range = [0, 1, 2, 3, 4]
#         co_range = [0, 1, 2, 3, 4]
#     elif mHow == 1:
#         mca = mCode - 1
#         ca_range = [mca]
#         co_range = [0, 1, 2, 3, 4]
#     elif mHow == 2:
#         mco = mCode - 1
#         co_range = [mco]
#         ca_range = [0, 1, 2, 3, 4]

#     top_5 = []
#     for mca in ca_range:
#         for mco in co_range:
#             base_dict = discount_list[mca][mco]
#             for z in range(120):
#                 bucket = market_list[mca][mco][z]
#                 if not bucket:
#                     continue

#                 for idx, val in bucket.items():
#                     cur_price = val[2] - base_dict
#                     if cur_price <= 0:
#                         continue
                        
#                     entry = (-cur_price, -idx)
#                     if len(top_5) < 5:
#                         heapq.heappush(top_5, entry)
#                     else:
#                         if entry > top_5[0]:
#                             heapq.heapreplace(top_5, entry)
#     king_5 = []
#     while top_5:
#         val, idx = heapq.heappop(top_5)
#         king_5.append((-val, -idx))
    

#     king_5.sort(key=lambda x: (x[0], x[1]))

#     ans = min(5, len(king_5))
#     ans_list = [0, 0, 0, 0, 0]
#     for i in range(ans):
#         ans_list[i] = king_5[i][1]

#     return RESULT(ans, ans_list)



##### solution.py
class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5


# -----------------------------------------------------------
# 전역 자료구조 (네 형식 유지 + 성능용 구조 추가)
# -----------------------------------------------------------
market_list = [[[[] for _ in range(120)] for _ in range(5)] for _ in range(5)]
discount_list = [[0 for _ in range(5)] for _ in range(5)]
id_list = [[[] for _ in range(5)] for _ in range(5)]

# ★ 추가 1) mID의 위치를 바로 찾기 위한 인덱스: mID -> (mca, mco, bucket_idx)
midx = dict()

# ★ 추가 2) (카테고리, 제조사)별 base_value 최소 힙
#     - 원소: (base_value, mID)
#     - base_value = mPrice + "그때의" 누적할인 (sell 시 저장)
pair_heap = [[[] for _ in range(5)] for _ in range(5)]


def init():
    global market_list, discount_list, id_list, midx, pair_heap
    market_list = [[[{} for _ in range(120)] for _ in range(5)] for _ in range(5)]
    discount_list = [[0 for _ in range(5)] for _ in range(5)]
    id_list = [[[] for _ in range(5)] for _ in range(5)]
    midx = {}
    pair_heap = [[[] for _ in range(5)] for _ in range(5)]


def sell(mID, mCategory, mCompany, mPrice):
    """
    - base_value = mPrice + (현재 누적할인) 저장
    - market_list에 넣고, 위치 인덱스 midx에 기록
    - pair_heap[mca][mco]에 (base_value, mID) push → 할인/조회 최적화용
    - 반환: 해당 (품목, 제조사) 전체 판매 중 개수
    """
    import heapq
    global market_list, discount_list, id_list, midx, pair_heap

    bucket_idx = mPrice // 10000
    if bucket_idx > 119:  # 방어
        bucket_idx = 119

    mca = mCategory - 1
    mco = mCompany - 1
    base_value = mPrice + discount_list[mca][mco]

    market_list[mca][mco][bucket_idx][mID] = [mca, mco, base_value]
    id_list[mca][mco].append(mID)
    midx[mID] = (mca, mco, bucket_idx)

    heapq.heappush(pair_heap[mca][mco], (base_value, mID))

    # 같은 (카테고리, 제조사) 전체 개수 반환 (버킷 길이 합산: 120번 → 매우 싸다)
    total = 0
    for i in range(120):
        total += len(market_list[mca][mco][i])
    return total


def closeSale(mID):
    """
    - 인덱스로 즉시 위치 찾고 제거 → O(1)
    - 현재가(>0)면 가격 반환, 아니면 -1
    """
    global market_list, discount_list, midx

    pos = midx.get(mID)
    if not pos:
        return -1

    mca, mco, bucket_idx = pos
    item = market_list[mca][mco][bucket_idx].get(mID)
    if not item:
        # 인덱스만 남은 유령일 수도 있으니 정리
        midx.pop(mID, None)
        return -1

    cur_price = item[2] - discount_list[mca][mco]

    # 실제 종료 처리
    market_list[mca][mco][bucket_idx].pop(mID, None)
    midx.pop(mID, None)

    return cur_price if cur_price > 0 else -1


def discount(mCategory, mCompany, mAmount):
    """
    - 누적할인 갱신
    - pair_heap의 top(base_value)가 누적할인 이하일 동안 꺼내며 실제 데이터에서 제거
      (유효성은 midx/market_list로 확인 → lazy clean)
    - 반환: 해당 (품목, 제조사) 현재 판매 중 개수 (버킷 합산)
    """
    import heapq
    global market_list, discount_list, midx, pair_heap

    mca = mCategory - 1
    mco = mCompany - 1

    # 누적 할인액 갱신
    discount_list[mca][mco] += mAmount
    amount = discount_list[mca][mco]

    hp = pair_heap[mca][mco]
    # base_value <= amount 인 동안 삭제 (누적적으로 한 번씩만 제거됨 → 전체 O(N log N))
    while hp and hp[0][0] <= amount:
        base_value, mid = heapq.heappop(hp)

        pos = midx.get(mid)
        if not pos:
            # 이미 closeSale 등으로 지워진 유령 → skip
            continue

        # 실제로 존재하면 삭제
        p_mca, p_mco, bucket_idx = pos
        if p_mca == mca and p_mco == mco:
            # 방어적으로 dict에도 있는지 확인
            if mid in market_list[mca][mco][bucket_idx]:
                market_list[mca][mco][bucket_idx].pop(mid, None)
            midx.pop(mid, None)
        # (쌍이 다를 일은 없음. 혹시 몰라서 두었지만 실상 발생 X)

    # 남은 개수(버킷 합계) 반환
    alive = 0
    for idx in range(120):
        alive += len(market_list[mca][mco][idx])
    return alive


def show(mHow, mCode):
    """
    - 각 (카테고리, 제조사) 쌍의 pair_heap에서 '현재가'가 가장 싼 후보만 뽑아
      k-way 병합으로 상위 5개를 구함.
    - 현재가 = base_value - discount_list[mca][mco]
      (같은 쌍 내에서는 base_value 정렬 == 현재가 정렬)
    - show는 데이터 변경 없이 보기만 하므로, pair_heap에서 pop 한 원소는
      임시 보관 후 마지막에 되돌려 놓음(살아있는 것만).
    """
    import heapq
    global market_list, discount_list, midx, pair_heap

    # 1) 조회 범위
    if mHow == 0:
        ca_range = [0, 1, 2, 3, 4]
        co_range = [0, 1, 2, 3, 4]
    elif mHow == 1:
        mca = mCode - 1
        ca_range = [mca]
        co_range = [0, 1, 2, 3, 4]
    else:  # mHow == 2
        mco = mCode - 1
        co_range = [mco]
        ca_range = [0, 1, 2, 3, 4]

    # 2) (쌍별) pop 한 원소를 되돌리기 위한 임시 보관소
    popped_alive = [[[] for _ in range(5)] for _ in range(5)]

    # 3) 쌍에서 "다음 살아있는 후보"를 얻는 함수 (pop 하되, alive만 임시 저장)
    def next_alive_from_pair(pa, pb):
        hp = pair_heap[pa][pb]
        disc = discount_list[pa][pb]
        while hp:
            bv, mid = heapq.heappop(hp)  # 잠시 꺼냄
            # 살아있는가? midx에 있고, 같은 쌍이며, 현재가>0 이어야 함
            pos = midx.get(mid)
            if (not pos) or pos[0] != pa or pos[1] != pb:
                # 유령/무관한 건 폐기 (힙 청소 효과)
                continue
            cur_price = bv - disc
            if cur_price <= 0:
                # 할인으로 이미 죽었어야 하는 항목 → 청소만 하고 폐기
                # (discount에서 대부분 제거하지만 혹시 남았으면 여기서 힙 정리)
                continue
            # 유효 후보 → 임시로 보관(나중에 힙에 되돌릴 것)
            popped_alive[pa][pb].append((bv, mid))
            return (cur_price, mid, bv)
        return None

    # 4) 후보 프런티어: (현재가, ID, mca, mco, base_value)
    frontier = []
    for pa in ca_range:
        for pb in co_range:
            cand = next_alive_from_pair(pa, pb)
            if cand:
                cur_price, mid, bv = cand
                heapq.heappush(frontier, (cur_price, mid, pa, pb, bv))  # 가격 오름, 동가면 ID 오름

    # 5) 상위 5개 뽑기 (k-way 병합)
    ans_list = []
    while frontier and len(ans_list) < 5:
        cur_price, mid, pa, pb, bv = heapq.heappop(frontier)
        ans_list.append(mid)
        # 같은 쌍에서 다음 후보 가져와 넣기
        cand = next_alive_from_pair(pa, pb)
        if cand:
            n_price, n_mid, n_bv = cand
            heapq.heappush(frontier, (n_price, n_mid, pa, pb, n_bv))

    # 6) 힙 복구: show는 읽기 전용이므로, 꺼낸 살아있는 원소는 다시 푸시
    for pa in ca_range:
        for pb in co_range:
            hp = pair_heap[pa][pb]
            for item in popped_alive[pa][pb]:
                heapq.heappush(hp, item)

    # 7) RESULT 포맷으로 반환
    cnt = len(ans_list)
    IDs = [0, 0, 0, 0, 0]
    for i in range(cnt):
        IDs[i] = ans_list[i]
    return RESULT(cnt, IDs)
