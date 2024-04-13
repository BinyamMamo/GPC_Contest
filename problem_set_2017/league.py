"""
7th Gulf Programming Contest   
GUST 2017 
D. The Easy League 
"""
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def max_score(teams):
    return 2 * factorial(teams - 1) * 3


def main():
    cases = int(input().strip())
    for k in range(cases):
        teams = int(input().strip())
        print(f"{k + 1}. {max_score(teams)}")


if __name__ == "__main__":
    main()