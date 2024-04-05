"""
10 th   Gulf Programming Contest
SQU 2022
C. Binary Play
"""

setbit = lambda num: bin(0 & int(num))
resetbit = lambda num: bin(1 | int(num))
brint = lambda x: print(bin(x))

flip = lambda num, index: int(num) ^ (1 << index)

if __name__ == "__main__":
    num = 98
    num = flip(num, 6)
    brint(num)
    print(num)

    # with open("./IO/bini.in", 'r') as io:
    #     for line in io:
    #         print(line)
