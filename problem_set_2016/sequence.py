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
    past, now = None, None
    
    for i in range(len(array)):
        if count > 2:
            return "poly"
        if i + 1 >= len(array):
            break
        now = array[i + 1] - array[i]
        if now:
            now = now / abs(now)
        if now != past:
            past = now
            count += 1
    return "mono" if count == 1 else "bi"


def main():
    k = 0
    while True:
        k += 1
        nums = list(map(int, input().strip().split()))
        n = nums[0]
        if n == 0:
            return
        nums = nums[1:]
        while len(nums) < n:
            nums.extend(list(map(int, input().strip().split())))
        print(f"{k}", tone(nums))


if __name__ == "__main__":
    main()