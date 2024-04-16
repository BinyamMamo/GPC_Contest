"""
7th Gulf Programming Contest   
GUST 2017 
H. Armstrong numbers
"""
def is_armstrong(num):
    num = str(num)
    length = len(num)
    result = 0
    for n in num:
        result += int(n) ** length
    return result == int(num)


def main():
    cases = int(input().strip())
    for k in range(cases):
        num = int(input().strip())
        print(f"{k + 1}.", "yes" if is_armstrong(num) else "no")


if __name__ == "__main__":
    main()
