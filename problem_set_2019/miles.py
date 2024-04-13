"""
9th Gulf Programming Contest   
SQU 2019 
C. Miles of The Sky 
"""
def main():
    k = 0
    while True:
        k += 1
        m, valid = map(int, input().strip().split())
        if m == 0:
            return
        months = list(map(int, input().strip().split()))
        if len(months) <= valid:
            print(f"{k}. {sum(months)}")
            continue
        left, right = 0, valid
        tier = sum(months[:valid])
        max_tier = tier

        for _ in range(m):
            if right >= m:
                break
            tier = tier - months[left]
            tier = tier + months[right]
            max_tier = max(max_tier, tier)
            left += 1
            right += 1
        print(f"{k}. {max_tier}")

if __name__ == "__main__":
    main()