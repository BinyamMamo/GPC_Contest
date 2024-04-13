"""
9th Gulf Programming Contest   
SQU 2019 
A. The Purifier
"""

def main():
    cases = int(input().strip())
    for k in range(cases):
        xhrs, ydays = map(int, input().strip().split())
        ttl_hrs = 0
        for _ in range(ydays):
            try:
                day = list(input().strip().split())
            except EOFError:
                continue
            bzy_hr = 0
            for time in day:
                if time == "-":
                    continue
                time = time.replace(":", ".")
                hr1, hr2 = map(float, time.strip().split("-"))
                bzy_hr += abs(hr2 - hr1)
            ttl_hrs += 14 - bzy_hr
        print(f"{k + 1}.", "Yes" if ttl_hrs > xhrs else "No")


if __name__ == "__main__":
    main()