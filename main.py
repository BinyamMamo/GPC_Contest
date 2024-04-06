def intersection(set1, set2):
    common = []
    if set1 == set2:
        print("hello")
        return set1
    for s1 in set1:
        if s1 in set2 and s1 not in common:
            common.append(s1)
    return common

a = [1, 2, 3]
b = [1, 2, 3]
# b = []
print(intersection(a, b))
