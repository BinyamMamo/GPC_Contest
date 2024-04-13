"""
9th Gulf Programming Contest   
SQU 2019 
E. Fair share  
Input: fair.in
"""
from itertools import combinations, permutations

def find_fair_share(K, target, cake_set):
    # Generate all possible combinations of n-digit numbers
    nums = []
    for n in list(permutations(cake_set, target)):
        nums.append(int("".join(str(nn) for nn in n)))
    min_difference = target
    print(nums)
    # Calculate the difference for each combination
    left, right = 0, 1
    for left in range(len(nums)):
        if right >= len(nums):
            right = left

        num1 = nums[left]
        num2 = nums[right]
        difference = abs(num1 - num2)
        intr = set(str(num1)).intersection(set(str(num2)))
        if difference > 0 and len(intr) < 1:
            min_difference = min(min_difference, difference)
        left += 1
        right += 1

    # print("--------")
    return min_difference


def findmin(cakes, target):
    l = 0
    r = 1
    sub = []
    cakes.sort()
    while l < len(cakes):
        if r >= len(cakes):
            r = l
        diff = abs(cakes[r] - cakes[l])
        sub.append(diff)
        l += 1
        r += 1
    sub = sorted(sub)
    for s in sub:

        if sub.count(s) >= target and s > 0:
            return s
    return 0


def main():
    while True:
        line = list(map(int, input().strip().split()))
        k = int(line[0])
        if k == 0:
            break
        n = int(line[1])
        cakes = list(map(int, input().strip().split()))
        print("ans:", find_fair_share(k, n, set(cakes)))


if __name__ == "__main__":
    main()
