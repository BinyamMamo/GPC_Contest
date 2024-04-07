letters = [
    [[" ", "-", " "], ["|", " ", "|"], [" ", " ", " "], ["|", " ", "|"], [" ", "-", " "]],
    [[" ", " ", " "], [" ", " ", "|"], [" ", " ", " "], [" ", " ", "|"], [" ", " ", " "]],
    [[" ", "-", " "], [" ", " ", "|"], [" ", "-", " "], ["|", " ", " "], [" ", "-", " "]],
    [[" ", "-", " "], [" ", " ", "|"], [" ", "-", " "], [" ", " ", "|"], [" ", "-", " "]],
    [[" ", " ", " "], ["|", " ", "|"], [" ", "-", " "], [" ", " ", "|"], [" ", " ", " "]],
    [[" ", "-", " "], ["|", " ", " "], [" ", "-", " "], [" ", " ", "|"], [" ", "-", " "]],
    [[" ", "-", " "], ["|", " ", " "], [" ", "-", " "], ["|", " ", "|"], [" ", "-", " "]],
    [[" ", "-", " "], [" ", " ", "|"], [" ", " ", " "], [" ", " ", "|"], [" ", " ", " "]],
    [[" ", "-", " "], ["|", " ", "|"], [" ", "-", " "], ["|", " ", "|"], [" ", "-", " "]],
    [[" ", "-", " "], ["|", " ", "|"], [" ", "-", " "], [" ", " ", "|"], [" ", "-", " "]],
]


def print_digital(num, size=1, spacing=1):
    digits = [int(n) for n in str(num)]
    for i in range(5):
        if not i % 2:
            for j, d in enumerate(digits):
                lbar = letters[d][i][0]
                rbar = letters[d][i][2]
                print(lbar, str(letters[d][i][1]) * size, rbar, sep="", end="")  # TODO: end should not be space at END
                if j < len(digits) - 1:
                    print(" " * spacing, end="")
            print()
        else:
            for _ in range(size):
                for j, d in enumerate(digits):
                    lbar = letters[d][i][0]
                    rbar = letters[d][i][2]
                    print(lbar, " " * size, rbar, sep="", end="")  # TODO: end should not be space at END
                    if j < len(digits) - 1:
                        print(" " * spacing, end="")
                print()
    print()


if __name__ == '__main__':
    # print_digital(1234567890, 5, 10)
    while user_input := input("Enter a valid printing size and number: "):
        size, num = user_input.split(" ")
        num, size = int(num), int(size)
        if not size:
            break
        print_digital(num, size)  # no need for spacing

    print("bye!")
