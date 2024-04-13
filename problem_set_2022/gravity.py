"""
10 th   Gulf Programming Contest                                                                                                                                   
SQU 2022 
K. Your Weight On Other Worlds
"""

if __name__ == "__main__":
    with open("./in.in") as gravity:
        lines = gravity.readlines()

    with open('./out.out', 'w') as file:
        pass

    lines = iter(lines)
    for line in lines:
        cases = int(line.strip())
        for _ in range(cases):
            mass, planet, g = next(lines).strip().split()
            mass = int(mass)
            g = float(g)
            with open("./out.out", 'a', newline='\r\n') as gravity:
                print(f"Earth {mass * 10}N {planet} {mass * g:.1f}N",
                      file=gravity)
