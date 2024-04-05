"""
Gulf Programming Contest
SQU 2022
H. Areej Makeup Show

✅Successful 💪
"""

if __name__ == "__main__":
    with open("areej.in", 'r') as areej:
        for line in areej:
            vouchers, items = [int(n) for n in line.split(" ")]
            if not vouchers:
                break
            for _ in range(vouchers):
                votes_count = int(next(areej))
                votes = {}
                max = 0
                max_key = None
                for i in range(votes_count):
                    vote = next(areej).strip()
                    if votes.get(vote) is not None:
                        # print(votes.get(vote))
                        votes[vote] = votes.get(vote) + 1
                        if votes.get(vote) > max:
                            max = votes.get(vote)
                            max_key = vote
                    else:
                        votes[vote] = 0
                print(max_key)
            print()
