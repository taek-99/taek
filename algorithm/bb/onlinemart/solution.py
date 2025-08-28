class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

    price_list = [[] for _ in range(5)]
    mart_id_price = {}


def init():
    global price_list, mart_id_price
    price_list = [[] for _ in range(5) for _ in range(5)]
    mart_id_price = {}
    

def sell(mID, mCategory, mCompanym,Price):
    global price_list, mart_id_price
    price_list[mCategory-1][mCompanym-1].append(Price)
    
    mart_id_price[mID] = [mCategory-1, mCompanym-1, len(price_list[mCategory-1][mCompanym-1])-1]

    return len(price_list[mCategory-1][mCompanym-1])

def closeSale(mID):
    global price_list, mart_id_price
    x = mart_id_price[mID][0]
    y = mart_id_price[mID][1]
    z = mart_id_price[mID][2]
    
    ans = -1
    if price_list[x][y][z] > 0:
        ans = price_list[x][y][z]

    return ans

def discount(mCategory, mCompany, mAmount):
    x = mCategory-1
    y = mCompany-1
    
    for idx in range(len(price_list[x][y])):
        aaa = price_list[x][y][idx] - mAmount
        if aaa < 0:
            price_list[x][y].remove(price_list[x][y][idx])
            mart_id_price[x, y, idx].remove(price_list[x][y][idx])

        price_list[x][y][idx] = aaa

    return len(price_list[x][y])

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