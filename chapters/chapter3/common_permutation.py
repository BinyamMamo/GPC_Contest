"""
Common Permutation 
PC/UVa IDs: 110303/10252 
Popularity: A Success rate: average 
Level: 1
"""
import sys


def common(str1, str2):
    if str2 is None:
        return None

    result = []
    str1, str2 = str1.strip(), str2.strip()
    for s in str1:
        if s in str2:
            result.append(s)

    return "".join(sorted(result))


def main():
    for line in sys.stdin:
        print(common(line, next(sys.stdin, None)))


if __name__ == "__main__":
    main()
