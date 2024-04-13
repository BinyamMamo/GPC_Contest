"""
10 th   Gulf Programming Contest                                                                                                                                   
SQU 2022 
D.  Virus Outbreak
Program: virus.(cpp|java)
Input: virus.in
"""

def recur(q1, q2, database):
    v1 = q1.split("_")[0]  # virus
    v2 = q2.split("_")[0]
    p1 = q1  # parent
    p2 = q2
    for d in database:
        if d.split("_")[1] == v1:
            p1 = d
            if d.split("_")[1] == v2:
                return d
        if d.split("_")[1] == v2:
            p2 = d
            if d.split("_")[1] == v1:
                return d
    print(p1, p2)
    if p1 == p2 or p1 is None or p2 is None:
        return p1
    return recur(p1, p2, database)

def seek_origin(query, database):
    origins = []
    virus = query.split("_")[0]  # virus
    while virus != "000":
        for dna in database:
            if dna.split("_")[1] == virus:
                origins.append(dna)
                virus = dna.split("_")[0]
                break
    return origins

def origin(queries, database):
    origins = set(seek_origin(queries[0], database))
    for q in queries:
        origins.intersection_update(seek_origin(q, database))
    origins = list(origins)
    # if origins:
    return origins
    return "000_000"
    a = reversed(a)
    origin = "000_000"
    for item in a:
        if item in b:
            origin = item
    return origin


with open("./io/virus.in", 'r') as virus:
    d, q = map(int, virus.readline().strip().split())
    while d != 0:
        database = virus.readline().strip().split()
        for k in range(q):
            queries = virus.readline().strip().split()
            # print(queries, recur(queries[0], queries[1], database))
            print(origin(queries, database))
            # print("------------------")
        d, q = map(int, virus.readline().strip().split())
