#로컬에서 테스트 시
#solution.py와 main.py 파일을 구분해 주세요.
#main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.

#제출 시 solution.py 부분만 변경하여 제출해 주세요.

#####solution.py
class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

<<<<<<< HEAD
market_list = [[[[] for _ in range(120)] for _ in range(5)] for _ in range(5)] 
discount_list = [[0 for _ in range(5)] for _ in range(5)] 
id_list = [[[] for _ in range(5)] for _ in range(5)] 


def init():
    global market_list, discount_list, id_list

    market_list = [[[[] for _ in range(120)] for _ in range(5)] for _ in range(5)] 
    discount_list = [[0 for _ in range(5)] for _ in range(5)] 
    id_list = [[[] for _ in range(5)] for _ in range(5)] 


def sell(mID, mCategory, mCompany, mPrice):
    global market_list, discount_list, id_list
    
    bucket_idx = mPrice // 10000
    mca = mCategory - 1
    mco = mCompany - 1
    price = mPrice + discount_list[mca][mco]
=======
    price_list = [[[] for _ in range(5)] for _ in range(5)]
    discount_list = [[0 for _ in range(5)] for _ in range(5)]
    mid_list = [[[] for _ in range(5)] for _ in range(5)]
    mart_id_price = {}


def init():
    global price_list, mart_id_price, discount_list, mid_list
    price_list = [[[] for _ in range(5)] for _ in range(5)]
    discount_list = [[0 for _ in range(5)] for _ in range(5)]
    mid_list = [[[] for _ in range(5)] for _ in range(5)]
    mart_id_price = {}

def sell(mID, mCategory, mCompanym, Price):
    global price_list, mart_id_price, mid_list, discount_list
    mca = mCategory - 1
    mco = mCompanym - 1
    heapq.heappush(price_list[mca][mco], Price+discount_list[mca][mco])  # 애초에 힙푸쉬로 입력
    
    mart_id_price[mID] = [mca, mco, Price]  # Mid 딕셔너리
    mid_list[mca][mco].append(mID)
>>>>>>> 52ffc52bed26a23a3921d0289ecdc29000175de2

    data = {
        mID : [mca, mco, price]
    }

    # print (mca,mco,bucket_idx, data)
    market_list[mca][mco][bucket_idx].append(data)
    # print (market_list[mca][mco][bucket_idx])
    id_list[mca][mco].append(mID)

    return len(market_list[mca][mco][bucket_idx])

def closeSale(mID):
    global market_list, discount_list, id_list

    for mca in range(5):
        for mco in range(5):
            for idx in range(120):
                if market_list[mca][mco][idx]:
                    for val in market_list[mca][mco][idx]:
                        market_key = list(val.keys())[0]
                        market_val = list(val.values())[0][2]
                        if market_key == mID:
                            if market_val - discount_list[mca][mco] > 0:
                                return market_val - discount_list[mca][mco]
                            else:
                                return -1
    return -1

def discount(mCategory, mCompany, mAmount):
    global market_list, discount_list, id_list

<<<<<<< HEAD
    mca = mCategory - 1
    mco = mCompany - 1
    amount = discount_list[mca][mco] + mAmount

    for idx in range(120):
        num = idx * 10000
        if num > amount:
            count_idx = idx
=======
    discount_list[mca][mco] += mAmount
    
    while True:
        print (mca, mco)
        print ()
        hh = heapq.heappop(price_list[mca][mco])
        if hh - mAmount > 0:
            heapq.heappush(price_list[mca][mco], hh)
>>>>>>> 52ffc52bed26a23a3921d0289ecdc29000175de2
            break

        if market_list[mca][mco][idx]:
            market_list[mca][mco][idx] = []


    cnt = 0
    for idx in range(count_idx, 120):
        if idx == count_idx:
            for val in market_list[mca][mco][idx]:
                if market_list[mca][mco][idx][val][2] > amount:
                    cnt += 1
        else:
            if market_list[mca][mco][idx]:
                cnt += len(market_list[mca][mco][idx])

    return cnt

def show(mHow, mCode):
    return RESULT(-1, [0, 0, 0, 0, 0])
