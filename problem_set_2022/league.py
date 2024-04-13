"""
10 th   Gulf Programming Contest
SQU 2022
I. The League
"""


with open("./io/league.out", 'w', newline="\r\n") as league:
    pass


with open("./io/league.in", 'r') as league:
    cases = int(league.readline().strip())
    with open("./io/league.out", 'a', newline="\r\n") as output:
        for k in range(cases):
            line = league.readline().strip().split()
            div, season, pro, rel = map(int, line)
            if pro + rel <= season:
                print(f"{k + 1}. {div - (pro - rel)}", file=output)
