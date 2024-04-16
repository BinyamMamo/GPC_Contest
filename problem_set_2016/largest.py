"""
6th Gulf Programming Contest   GUST 2016 
15/17 
Problem I 
Largest Number 
 
Source file:  largest.{c | cpp | java} 
Input file:  largest.in
"""
from itertools import permutations
def largest(nums):
    result = []
    permutation = list(permutations(nums))
    for nums in permutation:
        result.append(int("".join([str(n) for n in nums])))
    return max(result)


def main():
    test_cases = int(input().strip())
    for _ in range(test_cases):
        nums = list(map(int, input().strip().split()))
        nums = nums[1:]
        print(largest(nums))


if __name__ == "__main__":
    main()