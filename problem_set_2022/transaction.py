"""
10 th   Gulf Programming Contest                                                                                                                                   
SQU 2022 
G. Transaction frequency
"""

from itertools import combinations
# from collections import Counter

def Counter(items):
    result = {}
    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

def Combinations(st, k):
    result = []
    for s in st:
        for ss in st:
            buffer = ""
            for _ in range(k):
                if s not in ss:
                    buffer += ss
            result.append(buffer)
    return result

def transaction_frequency():
    with open("io/transaction.in", "r") as transaction:
        lines = transaction.readlines()

    while True:
        N = int(input())
        if N == 0:
            break

        transactions = [input().strip() for _ in range(N)]
        S, k = map(int, input().split())

        item_sets = []
        for transaction in transactions:
            print(transaction)
            for item_set in combinations(sorted(transaction), k):
                item_sets.append(''.join(item_set))

        counter = Counter(item_sets)
        # print(counter)
        print(sum(1 for item_set, freq in counter.items() if freq >= S))

if __name__ == "__main__":
    transaction_frequency()
# end main
