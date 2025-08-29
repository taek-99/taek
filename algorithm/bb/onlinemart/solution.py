#로컬에서 테스트 시
#solution.py와 main.py 파일을 구분해 주세요.
#main.py의 import와 from와 sys.stdin 주석을 해제해 주세요.

#제출 시 solution.py 부분만 변경하여 제출해 주세요.

#####solution.py
class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5


market_list = [[[[] for _ in range(120)] for _ in range(5)] for _ in range(5)] 
discount_list = [[0 for _ in range(5)] for _ in range(5)] 
id_list = [[[] for _ in range(5)] for _ in range(5)] 


def init():
    global market_list, discount_list, id_list

    market_list = [[[{} for _ in range(120)] for _ in range(5)] for _ in range(5)] 
    discount_list = [[0 for _ in range(5)] for _ in range(5)] 
    id_list = [[[] for _ in range(5)] for _ in range(5)] 


def sell(mID, mCategory, mCompany, mPrice):
    global market_list, discount_list, id_list
    
    bucket_idx = mPrice // 10000
    mca = mCategory - 1
    mco = mCompany - 1
    price = mPrice + discount_list[mca][mco]

    market_list[mca][mco][bucket_idx][mID] = [mca, mco, price]
    id_list[mca][mco].append(mID)

    return len(market_list[mca][mco][bucket_idx])

def closeSale(mID):
    global market_list, discount_list, id_list

    for mca in range(5):
        for mco in range(5):
            for idx in range(120):
                if market_list[mca][mco][idx]:
                    for num, val in market_list[mca][mco][idx].items():
                        if num == mID:
                            if val[2] - discount_list[mca][mco] > 0:
                                return val[2] - discount_list[mca][mco]
                            else:
                                return -1
    return -1

def discount(mCategory, mCompany, mAmount):
    global market_list, discount_list, id_list
    
    mca = mCategory - 1
    mco = mCompany - 1
    amount = discount_list[mca][mco] + mAmount
    discount_list[mca][mco] = amount

    for idx in range(120):
        num = idx * 10000

        if amount < 10000:
            count_idx = idx
            break

        if num > amount:
            count_idx = idx
            break

        if market_list[mca][mco][idx]:
            market_list[mca][mco][idx] = {}

    cnt = 0
    del_dict = {}
    for idx in range(count_idx, 120):
        if idx == count_idx:
            for num, val in market_list[mca][mco][idx].items():
                if val[2] > amount:
                    cnt += 1
                else:
                    del_dict[num] = val
        else:
            if market_list[mca][mco][idx]:
                cnt += len(market_list[mca][mco][idx])

    for k in del_dict.keys():
        market_list[mca][mco][count_idx].pop(k, None)

    return cnt

def show(mHow, mCode):
    return RESULT(-1, [0, 0, 0, 0, 0])
