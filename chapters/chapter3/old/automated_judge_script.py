"""
Automated Judge Script 
PC/UVa IDs: 110305/10188 
Popularity: B 
Success rate: average 
Level: 1 
"""
def parse_int(array):
    result = []
    for item in array:
        num = 0
        for char in item:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char != " ":
                result.append(num)
                num = 0
    return result


def compare(correct, submitted):
    if correct == submitted:
        return "Accepted"

    numeric_correct = parse_int(correct)
    numeric_submitted = parse_int(submitted)
    print(numeric_correct, numeric_submitted)
    return None


def main():
    k = 0
    while True:
        k += 1
        try:
            both = []
            for _ in range(2):
                solutions = []
                n = int(input().strip())
                if n == 0:
                    return

                for _ in range(n):
                    solutions.append(input().strip())
                both.append(solutions)
            print(f"Run #{k}:", compare(both[0], both[1]))
        except EOFError:
            return


if __name__ == "__main__":
    main()