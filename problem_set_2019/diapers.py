"""
9th Gulf Programming Contest   
SQU 2019 
J. The Legend of Diapers  
Description 
Program:            
Input:                 
diapers.(cpp|java|py) 
diapers.in 
Balloon Color:   Brown 
"""

def main():
    with open("out.out", 'w', newline="\r\n") as output:
        pass
    with open("in.in", 'r') as diapers:
        cases = int(diapers.readline().strip())
        with open("out.out", 'a', newline="\r\n") as output:
            for k in range(cases):
                total, daily = map(int, diapers.readline().strip().split())
                print(f"{k + 1}. {total // daily}", file=output)


if __name__ == "__main__":
    main()