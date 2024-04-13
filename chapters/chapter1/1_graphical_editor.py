"""
Graphical editor
PC/UVa IDs: 110105/10267 
Popularity: B 
Success rate: low 
Level: 1
"""

class Graphics:
    def __init__(self, m=None, n=None):
        self.M = m
        self.N = n
        self._canvas = None
        self.commands = {
            "I": self.createImage,
            "C": self.clear,
            "L": self.pixel,
            "K": self.fill,
            "F": self.fillR,
            "S": self.save,
            "X": self.quit,
            "V": self.fillV,
            "H": self.fillH,
        }

    def createImage(self, m, n):
        self.M = m
        self.N = n
        self._canvas = [['O' for _ in range(self.M)] for _ in range(self.N)]

    def clear(self):
        self.fill(0, 0, self.M, self.N, "O")

    def pixel(self, x: int, y: int, c: str) -> None:
        self._canvas[int(y) - 1][int(x) - 1] = c

    def fillH(self, x1, x2, y, c):
        for i in range(int(x1)-1, int(x2)):
            self._canvas[int(y)-1][i] = c

    def fillV(self, x, y1, y2, c):
        for i in range(int(y1)-1, int(y2)):
            self._canvas[i][int(x)-1] = c


    def fill(self, x1, y1, x2, y2, c):
        for i in range(int(y1) - 1, int(y2)):
            for j in range(int(x1) - 1, x2):
                self._canvas[i][j] = c

    def _recurse(self, x, y, c, target):
        if x < 0 or x >= self.M or y < 0 or y >= self.N:
            return
        if self._canvas[y][x] != target or self._canvas[y][x] == c:
            return
        self._canvas[y][x] = c
        self._recurse(x + 1, y, c, target)
        self._recurse(x - 1, y, c, target)
        self._recurse(x, y + 1, c, target)
        self._recurse(x, y - 1, c, target)

    def fillR(self, x, y, c):
        target = self._canvas[int(y) - 1][int(x) - 1]
        self._recurse(int(x) - 1, int(y) - 1, c, target)

    def _msdos83(self, filename):
        name, ext = filename.rsplit('.', 1) if '.' in filename else (filename, '')
        name = name[:6].upper() + '~1' if len(name) > 6 else name.upper()
        ext = (ext[:3]).upper()
        return f"{name}.{ext}" if ext else name

    def save(self, name):
        # print(self._msdos83(name))
        print(name)
        for row in self._canvas:
            print("".join(row))

    def quit(self):
        exit()

    def help(self):
        print("usage: COMMAND [PARAMETERS]")
        print("Terminal based simple interactive graphical editor.")
        print()
        print("Supported commands:")
        print(", ".join(self.commands))
        # for cmd in self.commands:
        #     print(" - ", cmd)

    def get_command(self, line):  # TODO: ? TO CARE ABOUT CAPITALIZATION
        args = line.strip().split(" ")
        cmd, params = args[0], args[1:]
        params = [p for p in params if (p != "" and p is not None)]
        params = [int(p) if p.isdigit() else p for p in params]
        if cmd in self.commands:
            func = self.commands[cmd]
            func(*params)
        # else:
        #     if cmd == "help":
        #         self.help()
        #     else:
        #         print(cmd, ": Command not found", sep="")
        #         print("Type help for list of available commands")

if __name__ == '__main__':
    canvas = Graphics()
    while True:
        # user_input = input("> ")
        user_input = input("")
        canvas.get_command(user_input)
