"""
6th Gulf Programming Contest   GUST 2016 
15/17 
Problem I 
Largest Number 
 
Source file:  largest.{c | cpp | java} 
Input file:  largest.in
"""
def largest(nums):
    nums = sorted(nums, reverse=True)
    return sorted(nums, key=lambda x: int(str(x)[0]), reverse=True)


def main():
    test_cases = int(input().strip())
    for _ in range(test_cases):
        nums = list(map(int, input().strip().split()))
        nums = nums[1:]
        print(largest(nums))


if __name__ == "__main__":
    main()