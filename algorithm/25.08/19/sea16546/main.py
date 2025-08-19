import sys
sys.stdin = open('input (26).txt', 'r')

from itertools import permutations

T = int(input())

for tc in range(1, T+1):
    n = input()
    num_list = list(map(int, n.strip()))

    def is_run(cards):
        return cards[0] == cards[1] -1 == cards[2] - 2

    def is_triplet(cards):
        return cards[0] == cards[1] == cards[2]

    def is_babygin(cards):
        for perm in permutations(cards):
            fir_group = perm[:3]
            sec_group = perm[3:]

            if (is_run(fir_group) or is_triplet(fir_group)) and (is_run(sec_group) or is_triplet(sec_group)):
                return True

        return False

    if is_babygin(num_list):
        print (f"#{tc} true")
    else:
        print(f"#{tc} false")