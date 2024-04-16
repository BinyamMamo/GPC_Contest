"""
8th Gulf Programming Contest   
Zayed Univ. 2018 
D. Flu Epidemic
"""
class Solution:
    def __init__(self):
        self.room = []
        self.cured_after = None
        self.inc_period = None
        self.infect_rad = None
        self.staying_duration = None

    def run(self):
        while True:
            w, h = map(int, input().strip().split())
            if w == 0 and h == 0:
                return

            self.cured_after, self.inc_period, self.infect_rad, self.staying_duration = map(int, input().strip().split())
            self.room = []
            for _ in range(h):
                self.room.append(list(input().strip()))
            for row in self.room:
                print(row)

            print(self.count_infected())

    def count_infected(self):
        return 5


if __name__ == "__main__":
    s = Solution()
    s.run()
