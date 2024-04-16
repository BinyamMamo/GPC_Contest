"""
6th Gulf Programming Contest   GUST 2016 
15/17 
Problem I 
Largest Number 
 
Source file:  largest.{c | cpp | java} 
Input file:  largest.in
"""
def largest(nums):
    num1 = sorted(nums, reverse=True)
    num2 = sorted(nums, key=lambda x: int(str(x)[0]), reverse=True)
    num3 = sorted(nums, key=lambda x: len(str(x)))
    num1 = int("".join([str(n) for n in num1]))
    num2 = int("".join([str(n) for n in num2]))
    num3 = int("".join([str(n) for n in num3]))
    return max(num1, num2, num3)


def main():
    test_cases = int(input().strip())
    for _ in range(test_cases):
        nums = list(map(int, input().strip().split()))
        nums = nums[1:]
        print(largest(nums))


if __name__ == "__main__":
    main()