"""
9th Gulf Programming Contest   
SQU 2019 
D.  Take that Photo 
"""
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def count_duplicate(array):
    visited = set()
    count = {}
    for item in array:
        if array.count(item) > 1:
            if count.get(item) is None:
                count[item] = 0
            else:
                count[item] += 1
    return count


def photo(children):
    result = 1
    dup_count = count_duplicate(children)
    for key, count in dup_count.items():
        result *= factorial(count + 1)
    return result


def main():
    # print(factorial(4))
    # return 1
    cases = int(input().strip())
    for k in range(cases):
        line = list(map(int, input().strip().split()))
        children = line[1:]
        print(f"{k + 1}. {photo(children)}")


if __name__ == "__main__":
    main()
