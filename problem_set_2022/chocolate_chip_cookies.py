"""
Chocolate Chip Cookies
"""
import math


class Point:
    def __init__(self, x, y, r=0):
        self.x = x
        self.y = y
        self.r = r

cl = Point(None, None)  # cleft - pointer on circle at left
cr = Point(None, None)  # cright - pointer on circle at right

def dist_p2p(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def circle(a, b, r):
    dist_c2ab = math.sqrt(abs(r**2 - dist_p2p(a, b)**2 / 4))
    if a.x == b.x:
        cl.y = cr.y = (a.y + b.y) / 2
        cl.x = a.x + dist_c2ab
        cr.x = a.x - dist_c2ab
        cl.x = a.x - dist_c2ab
        cr.x = a.x + dist_c2ab
    else:
        k = math.atan((b.x - a.x) / (a.y - b.y))
        cl.x = (a.x + b.x) / 2 + dist_c2ab * math.cos(k)
        cl.y = (a.y + b.y) / 2 + dist_c2ab * math.sin(k)
        cr.x = (a.x + b.x) / 2 - dist_c2ab * math.cos(k)
        cr.y = (a.y + b.y) / 2 - dist_c2ab * math.sin(k)


RADIUS = 2.5
def main():
    with open("in.in", "r") as chips:
        lines = chips.readlines()
    
    output = ""
    lines = iter(lines)
    for line in lines:
        n = int(line.strip())
        if n == 0:
            break
        for _ in range(n):
            P = []
            count = 0
            line = next(lines, None)  # skip an empty line
            line = next(lines, None)
            while line is not None and len(line) > 1:
                x, y = map(float, line.strip().split())
                P.append(Point(x, y))
                count += 1
                line = next(lines, None)

            max_count = 1
            for i in range(1, count):
                for j in range(i):
                    circle(P[i], P[j], RADIUS)
                    l_count = r_count = 0
                    for k in range(count):
                        if dist_p2p(P[k], cl) <= 2.5:
                            l_count += 1
                        if dist_p2p(P[k], cr) <= 2.5:
                            r_count += 1
                    max_count = max(max_count, l_count, r_count)

            print(max_count)
            output += f"{max_count}\n"
            print()  # to remove?

    with open("out.out", 'w', newline="\r\n") as chips:
        chips.write(output)

if __name__ == "__main__":
    main()
