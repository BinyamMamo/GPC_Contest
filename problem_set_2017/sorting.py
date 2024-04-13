"""
7th Gulf Programming Contest   
GUST 2017 
C. Table Sorting 
"""

def sort_rows(rows, instr):
    instr = reversed(instr)
    for i in instr:
        if i < 0:
            i = abs(i)
            rows = sorted(rows, key=lambda x: x[i - 1], reverse=True)
        else:
            rows = sorted(rows, key=lambda x: x[i - 1])
    return rows


def main():
    cases = int(input().strip())
    for k in range(cases):
        print("Table", k + 1)
        _, r, no_instr = map(int, input().strip().split())
        rows = []
        for _ in range(r):
            rows.append(input().strip().split())
        for i in range(no_instr):
            instr = list(map(int, input().strip().split()))
            instr.pop()
            print("Instruction", i + 1)
            for row in sort_rows(rows, instr):
                print(*row)


if __name__ == "__main__":
    main()