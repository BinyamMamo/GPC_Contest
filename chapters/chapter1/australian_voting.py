"""
Australian Voting 
 
PC/UVa IDs: 110108/10142
Popularity: B Success rate: low Level: 1
"""

def winner(candidates, votes):
    ballot = {n: 0 for n in range(len(candidates))}
    for vote in votes:
        i = 0
        while i < len(vote) and vote[i] > len(candidates):
            i += 1

        if vote[i] < len(candidates):
            ballot[vote[0] - 1] += 1
            break
    bigvote = max(ballot.values())
    count = 0
    for vote in ballot.values():
        if bigvote == vote:
            count += 1
        if count > 1:
            break
    if count > 1:
        del candidates[min(ballot, key=lambda x: ballot[x])]
        winner(candidates, votes)

    return candidates[max(ballot, key=lambda x: ballot[x])]

def main():
    with open("in.in", "r") as votes:
        lines = votes.readlines()
    
    lines = iter(lines)
    for line in lines:
        cases = int(line.strip())
        line = next(lines, None)
        for _ in range(cases):
            line = next(lines, None)
            no_cand = int(line.strip())
            candidates = []
            votes = []
            for _ in range(no_cand):
                candidates.append(next(lines, None).strip())
            while (line:=next(lines, None)) != None and len(line) > 1:
                votes.append(tuple(map(int, line.split())))
            # print(candidates)
            # print(votes)
            print(winner(candidates, votes))
            # print()


# line = next(lines, None)
if __name__ == "__main__":
    main()