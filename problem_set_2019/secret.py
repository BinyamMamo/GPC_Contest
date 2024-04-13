"""
9th Gulf Programming Contest   
SQU 2019 
I. The Secret Message 
"""
def dsecode(code):
    result = start = end = ""
    left = 0
    right = -1
    for i, c in enumerate(code):
        if c.isdigit():
            while c.isdigit():
                _, c = next(code, (-1, None))
            left = i
            start += code[left:i]

def decode(code):
    result = ""
    left = 0
    for i in range(len(code)):
        if code[i].isdigit():
            prev_index = i
            dig = int(code[i])
            while i < len(code) and code[i].isdigit():
                i += 1
            if dig % 2:
                result = result + code[left:prev_index]
            else:
                result = code[left:prev_index] + result
            left = i
    return result


if __name__ == "__main__":
    with open("out.out", 'w', newline='\r\n') as output:
        pass

    with open("in.in", "r") as secret:
        case = int(secret.readline().strip())
        with open("out.out", 'a', newline='\r\n') as output:
            for k in range(case):
                code = secret.readline().strip()
                print(f"{k + 1}. {decode(code)}", file=output)
