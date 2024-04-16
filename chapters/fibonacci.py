"""
Fibonacci
"""
def fibonacci(num1, num2):
    count = 0
    i = 1
    n = 1
    import math
    s = lambda x: math.sqrt(x)

    visited = set()
    num1, num2 = min(num1, num2), max(num1, num2)
    while True:
        if i >= num1 and i <= num2 and i not in visited:
            count += 1
            visited.add(i)
        if i >= num2:
            break
        i = 1/s(5)
        i *= (((1 + s(5)) / 2) ** n) - (((1 - s(5)) / 2) ** n)
        i = int(i)
        n += 1
    return count


def main():
    while True:
        num1, num2 = map(int, input().strip().split())
        if num1 == 0 and num2 == 0:
            return
        print(fibonacci(num1, num2))


if __name__ == "__main__":
    main()