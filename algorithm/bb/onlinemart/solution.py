import heapq

class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

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

    return len(price_list[mca][mco])

def closeSale(mID):
    global price_list, mart_id_price, mid_list, mid_list
    mca = mart_id_price[mID][0]
    mco = mart_id_price[mID][1]
    m_price = mart_id_price[mID][1]

    if m_price in price_list[mca][mco]:
        return m_price
    else:
        return -1

def discount(mCategory, mCompany, mAmount):
    global price_list, mart_id_price, discount_list, mid_list
    mca = mCategory-1
    mco = mCompany-1

    discount_list[mca][mco] += mAmount
    
    while True:
        print (mca, mco)
        print ()
        hh = heapq.heappop(price_list[mca][mco])
        if hh - mAmount > 0:
            heapq.heappush(price_list[mca][mco], hh)
            break
        else:
            for idx in mid_list[mca][mco]:
                if mart_id_price[idx][2] == hh:
                    closeSale(idx)

    return len(price_list[mca][mco])

def show(mHow, mCode):
    ans_list =[]
    ans_pos = set()

    for _ in range(5):
        min_num = 10 ** 10
        min_pos = (-1, -1)
        for i in range(5):
            for j in range(5):
                for k in range(len(price_list[i][j])):
                    if min_num > price_list[i][j][k] and min_pos not in ans_pos:
                        min_num = price_list[i][j][k]
                        min_pos = (i, j)

        if min_pos != (-1, -1):
            ans_list.append(min_num)


    return RESULT(-1, ans_list)