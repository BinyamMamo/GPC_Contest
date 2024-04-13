"""
Primary Arithmetic 
 
PC/UVa IDs: 110501/10035 Popularity: A Success rate: average Level: 1
"""

def carry(num1, num2):
    num1 = list(map(int, list(str(num1))))
    num2 = list(map(int, list(str(num2))))
    limit = -1 * min(1 + len(num1), 1 + len(num2))
    carry = 0
    count = 0
    for i in range(-1, limit, -1):
        s = num1[i] + num2[i] + carry
        if s >= 10:
            carry = s // 10
        else:
            carry = 0
        if carry > 0:
            count += 1
        num1[i] = s % 10
        num2[i] = s % 10
    if carry > 0:
        count += 1
    return count


def main():
    while True:
        num1, num2 = map(int, input().strip().split())
        if num1 == 0 and num2 == 0:
            return
        if value := carry(num1, num2):
            if value > 1:
                print(value, "carry operations.")
            else:
                print(value, "carry operation.")
        else:
            print("No carry operation.")

if __name__ == "__main__":
    main()