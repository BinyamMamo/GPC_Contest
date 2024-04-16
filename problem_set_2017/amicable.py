"""
7th Gulf Programming Contest   
GUST 2017 
I. Amicable Numbers
"""
def factor(num):
    result = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            result.append(i)
            if i != 1:
                result.append(num // i)
    return result


def amicable(num1, num2):
    factors1 = factor(num1)
    factors2 = factor(num2)
    return sum(factors1) == num2 and sum(factors2) == num1


def trim(input_text):
    return input_text.replace("\r", "\n").strip()


def main():
    cases = int(input().strip())
    for k in range(cases):
        num1, num2 = map(int, input().strip().split())
        print(f"{num1} {num2} are ",
              "not " if not amicable(num1, num2) else "",
              "amicable numbers", sep="")

if __name__ == "__main__":
    main()
