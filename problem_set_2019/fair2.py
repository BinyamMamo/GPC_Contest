def fair_share(digits, n):
  """
  Finds the minimum difference between two n-digit numbers formed from the given digits.

  Args:
      digits: A list of distinct digits (0-9).
      n: The number of digits for the constructed numbers.

  Returns:
      The minimum difference between two n-digit numbers formed from the digits.
  """
  digits.sort()  # Sort digits for efficient comparison
  min_diff = float('inf')
  for i in range(len(digits) - n + 1):
    first_num = int(''.join(digits[i:i+n]))
    second_num = int(''.join(digits[i+1:i+n+1]))
    min_diff = min(min_diff, abs(first_num - second_num))
  return min_diff

def main():
  """
  Reads input test cases and prints the fair share for each.
  """
  while True:
    k, n = map(int, input().split())
    if k == 0:
      break
    digits = list(map(int, input().split()))
    fairness = fair_share(digits, n)
    print(fairness)

if __name__ == "__main__":
  main()
