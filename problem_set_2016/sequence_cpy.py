"""
6th Gulf Programming Contest   
GUST 2016 
Problem A 
Ntonic Sequence 
Source file:  sequence.{c | cpp | java} 
Input file:  
sequence.in 
"""
def tone(array):
    count = 0
    conds = [
        lambda n1, n2 : n1 < n2,
        lambda n1, n2 : n1 > n2
    ]
    conds = iter(conds)
    cond = next(conds)
    array = iter(array)
    for item in array:
        if cond is None:
            return "poly"
        if cond(item, next(array, item)):
            continue
        cond = next(conds, None)
        count += 1
    return "bi" if count else "mono"


def main():
    k = 0
    while True:
        k += 1
        nums = list(map(int, input().strip().split()))
        n = nums[0]
        if n == 0:
            return
        print(f"{k}", tone(nums[1:]))


if __name__ == "__main__":
    main()