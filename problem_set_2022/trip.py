"""
J. The Company Trip
"""

def intersection(set1, set2):
    common = []
    if set1 == set2:
        return set1
    for s1 in set1:
        if s1 in set2 and s1 not in common:
            common.append(s1)
    return common

if __name__ == "__main__":
    with open("io/trip.in", "r") as trip:
        lines = trip.readlines()

    with open("io/trip.out", "w") as trip:
        trip.write("")
    output = ""
    lines = iter(lines)
    for line in lines:
        line = line.strip()
        cases = int(line)
        for k in range(cases):
            common = None
            employees = int(next(lines).strip())
            for _ in range(employees):
                countries = next(lines).split(" ")
                countries = countries[1:]
                countries = [int(c) for c in countries]
                if common is None:
                    common = countries
                common = intersection(common, countries)
            common = sorted(common)
            if len(common) < 1:
                output += f"{k + 1}. No Trip\n"
            else:
                common = ",".join(str(c) for c in common)
                output += f"{k + 1}. {common}\n"

    with open("io/trip.out", 'w', newline="\r\n") as trip:
        trip.write(output)
# end main