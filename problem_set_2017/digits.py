"""
7th Gulf Programming Contest   
GUST 2017 
L. The Digits
"""
def read(typed=int):
    return typed(input().strip())


def readline(typed=int):
    return map(typed, input().strip().split())


def count_char(num):
    spelling = {
        "0": 4,
        "1": 3,
        "2": 3,
        "3": 5,
        "4": 4,
        "5": 4,
        "6": 3,
        "7": 5,
        "8": 5,
        "9": 4
    }
    result = 0
    for digit in str(num):
        result += spelling.get(digit, 0)
    return result

def main():
    cases = read()
    for k in range(cases):
        num = read()
        print(f"{k + 1}.", count_char(num))

if __name__ == "__main__":
    main()