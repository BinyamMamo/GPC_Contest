"""
A. Dining Table
"""

def table(H, sara, tables):
    tables = sorted(tables)
    height = tables[0]
    for table in tables:
        if (sara > height):
            result = height
        print("Not possible")

if __name__ == "__main__":
    line = input("")
    i = 1
    target, sara, no_tables = 0, 0, 0
    while line and i < 2:
        line = line.strip()
        if i % 2:
            target, sara, no_tables = line.split(" ")
            target, sara, no_tables = float(target), float(sara), float(no_tables)
        else:
            lents = line.split(" ")
            lents = [float(l) for l in lents]
            table(target, sara, lents)
            print(lents)
        line = input("")
        i += 1
