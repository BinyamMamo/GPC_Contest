"""
graphical editor
"""
"""
            "V": self.fillV,
            "H": self.fillH,
"""

class Graphics:
    def __init__(self, w=None, h=None):
        self.width = w
        self.height = h
        self._canvas = None
        self.commands = {
            "I": self.createImage,
            "C": self.clear,
            "L": self.pixel,
            "K": self.fill,
            "F": self.fill_region,
            "S": self.save,
            "X": self.quit
        }

    def createImage(self, m, n):
        self.width = m
        self.height = n
        self._canvas = [["O"] * n for _ in range(m)]

    def clear(self):
        self.fill(0, 0, self.width, self.height, "O")

    def fillH(self, x1, x2, y, c):
        self.fill(x1, y, x2, y, c)

    def fillV(self, x, y1, y2, c):
        self.fill(x, y1, x, y2, c)

    def fill_region(self, x, y, c):
        oclr = self.clr(x, y)  #  old clr
        self.pixel(x, y, c)
        origin = (x, y)  #  old position
        pos = [x, y]
        count = 0
        while True:
            pos = [x - 1, y]
            if self.clr(*pos) == oclr:
                self.pixel(x - 1, y, c)
                count += 1
            pos = [x - 1, y]
            if self.clr(*pos) == oclr:
                self.pixel(x - 1, y, c)
                count += 1



            count += 1
        if self.clr(x, y) == pclr:
            self.pixel(x, y, c)

    def fill(self, x1, y1, x2, y2, c):
        for i in range(y1, y2):
            for j in range(x1, x2):
                self.pixel(i, j, c)

    def save(self, name):
        print(name)
        for i in range(self.height):
            for j in range(self.width):
                print(self._canvas[j][i], end="")
            print()

    def pixel(self, x: int, y: int, c: str) -> None:
        self._canvas[y][x] = c

    @property
    def clr(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        return self._canvas[y][x]
    def quit(self):
        exit(0)

    def get_command(self, line):  # TODO: ? TO CARE ABOUT CAPITALIZATION
        args = line.split(" ")
        cmd, params = args[0], args[1:]
        params = [p for p in params if (p != "" and p is not None)]
        params = [int(p) if p.isdigit() else p for p in params]
        if cmd in self.commands:
            func = self.commands[cmd]
            print(params, func)
            func(*params)

if __name__ == '__main__':
    canvas = Graphics()
    while True:
        user_input = input("Enter commmand: ")
        canvas.get_command(user_input)
