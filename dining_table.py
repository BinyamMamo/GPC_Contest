"""
A. Dining Table
"""

def check_tables(tables, sara, target):
    tables = list(enumerate(tables))
    for i, cur in tables:
        prev = tables[i - 1][1] if i > 0 else 0
        if cur - prev > sara:
            if prev > target:
                return "Not possible"
            return prev
        # Check if there is a next item
        if i + 1 < len(tables):
            _, nxt = tables[i + 1]
        else:
            nxt = None

        # If there is no next item, return "Not possible"
        if nxt is None:
            return "Not possible"
        if nxt - prev > sara:
            if prev > target:
                return "Not possible"
            return cur

if __name__ == "__main__":
    target, sara, no_tables = 0, 0, 0
    # with open("io/table.in", "r") as table:
    with open("io/table.in", "r") as table:
        lines = table.readlines()

    output = ""
    lines = iter(lines)
    for line in lines:
        cases = int(line.strip())
        for k in range(cases):
            line = next(lines)
            target, sara, no_tables = line.strip().split(" ")
            target, sara, no_tables = int(target), int(sara), int(no_tables)
            line = next(lines)
            tables = line.strip().split(" ")
            tables.append(target)
            tables = sorted(int(t) for t in tables)
            output += f"{k + 1}. {check_tables(tables, sara, target)}\n"  # you don't need \r\n here just \n is enough

    # sets the eof to crlf
    with open("io/table.out", "w", newline="\r\n") as table:
        table.write(output)
