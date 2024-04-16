"""
9th Gulf Programming Contest   
SQU 2019 
E. Fair share  
Input: fair.in
"""
from itertools import combinations, permutations
def calculate_fair_share(K, n, digits):
    # Sort the digits in ascending order
    digits = list(digits)
    digits.sort()

    # Construct the first n-digit number
    first_number = int("".join(map(str, digits[:n])))

    # Construct the second n-digit number
    second_number = int("".join(map(str, digits[-n:])))

    # Calculate the fair share (difference)
    fair_share = abs(first_number - second_number)
    return fair_share

def find_fair_share(K, target, cake_set):
    nums = []
    for n in list(permutations(cake_set, target)):
        nums.append(int("".join(str(nn) for nn in n)))

    print(nums)
    min_difference = float("inf")
    left, right = 0, 1
    for left in range(len(nums)):
        if right >= len(nums):
            right = left

        difference = abs(nums[left] - nums[right])
        intr = set(str(nums[left])).intersection(set(str(nums[right])))
        if difference > 0 and len(intr) < 1:
            min_difference = min(min_difference, difference)
        left += 1
        right += 1

    return min_difference


def main():
    while True:
        line = list(map(int, input().strip().split()))
        k = int(line[0])
        if k == 0:
            break
        n = int(line[1])
        cakes = list(map(int, input().strip().split()))
        print(calculate_fair_share(k, n, set(cakes)))


if __name__ == "__main__":
    main()
