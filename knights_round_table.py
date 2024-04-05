"""
The Knights of the Round Table
"""
import math


if __name__ == "__main__":
    line = input("")
    while line:
        a, b, c = line.split(" ")
        a, b, c = float(a), float(b), float(c)
        max = 1000000

        if a not in range(max) or b not in range(max) or c not in range(max):
            print("Invalid input")
            line = input("")
            continue
        s = (1/2)*(a + b + c)
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        radius = area / s
        print("The radius of the round table is:", round(radius, 3))
        line = input("")
