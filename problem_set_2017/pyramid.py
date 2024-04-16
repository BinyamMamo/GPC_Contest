"""
7th Gulf Programming Contest   
GUST 2017 
J. Number Pyramid
"""

def solve_pyramid(pyramid):
    for i in range(len(pyramid)-1, -1, -1):
        for j in range(len(pyramid[i])):
            if pyramid[i][j] == '-':
                if j + 1 >= len(pyramid[i]):
                    continue
                if i - 1 >= 0 and pyramid[i-1][j] != "-" and pyramid[i][j+1] != "-":
                    pyramid[i][j] = int(pyramid[i-1][j]) - int(pyramid[i][j+1])
    for row in pyramid:
        print(row)
    return pyramid[0][0]


def main():
    k = 0
    while True:
        k += 1
        d = input().strip()
        d = int(d)
        if d == -1:
            return
        pyramid = []
        for i in range(d):
            pyramid.append(list(map(str, input().split())))
        result = solve_pyramid(pyramid)
        print(f"{k}: {result}")


if __name__ == "__main__":
    main()
