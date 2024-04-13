"""
9th Gulf Programming Contest   
SQU 2019 
B. n Base Palindrome
"""


def base(n, b) -> str:
    if n < b:
        return str(n)
    if n % b < 10:
        remainder = f"{ n  % b}"
    else:
        remainder = f"{chr(ord('a') + ((n % b) - 10))}"
    return str(base(n // b, b)) + remainder


def is_palindrome(n, b):
    num = base(n, b)
    left, right = 0, len(num) - 1

    while left < right:
        if num[left] != num[right]:
            return False
        left += 1
        right += -1

    return True

def main():
    while True:
        n, b = map(int, input().strip().split())
        if n == 0 and b == 0:
            return 1
        print("Yes" if is_palindrome(n, b) else "No")


if __name__ == "__main__":
    main()





""" Old Code 

def base:
    r = []
    while n >= b:
        r.append(n % b)
        n = n // b
    r.append(n)
    r.reverse()
    print(r)

"""