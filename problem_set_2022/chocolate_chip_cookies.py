"""
Chocolate Chip Cookies
"""
import math

finals = []

def inside(center, point):
    x1, y1 = center[0], center[1]
    x2, y2 = point[0], point[1]
    r = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    print("r=", r)
    return r <= 2.5

if __name__ == "__main__":
    line = input("")
    dbline = 0
    coordinates = []
    while line or dbline < 2:
        if line:
            line = line.strip()
            x, y = line.split(" ")
            x, y = float(x), float(y)
            coordinates.append((x, y))
            line = input("")
        else:
            dbline += 1
    print(coordinates)
    counts = []
    for center in coordinates:
        count = 0
        for point in coordinates:
            if inside(center, point):
                count += 1
                finals.append((center, point))
                finals = list(set(finals))
        print("---------")
        counts.append(count)
    print(max(counts))
    print(counts)
    for f in sorted(finals):
        print(f)
