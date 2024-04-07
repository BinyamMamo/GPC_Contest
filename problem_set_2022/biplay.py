def count_flips(d, r):
    # Convert numbers to 24-bit binary strings
    d_bin = format(d, '024b')
    r_bin = format(r, '024b')
    
    # Count the number of different bits
    flip_default = sum(1 for i in range(24) if d_bin[i] != r_bin[i])
    ones = sum(1 for i in range(24) if r_bin[i] == '1')
    zeros = sum(1 for i in range(24) if r_bin[i] == '0')
    flip_ones = sum(1 for i in range(24) if "1" != r_bin[i])
    flip_ones += 1
    flip_zeros = sum(1 for i in range(24) if "0" != r_bin[i])
    flip_zeros += 1
    return min(flip_default, flip_ones, flip_zeros)

# Read input file
with open('io/biplay.in', 'r') as file:
    test_cases = file.readlines()

# Process each test case
output = []
for k, case in enumerate(test_cases, 1):
    d, r = map(int, case.split())
    if d == r == 0:
        break  # End of input
    ans = count_flips(d, r)
    output.append(f"{k}. {ans}")

# Write output to file
with open('io/biplay.out', 'w') as file:
    file.write('\n'.join(output))
    file.write('\n')
