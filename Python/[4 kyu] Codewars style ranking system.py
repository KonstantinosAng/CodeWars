# More details on this kata
# https://www.codewars.com/kata/51fda2d95d6efda45e00004e

# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
    def calc_progress(self, r):
        if r == 0 or r < -8 or r > 8 or self.rank < -8 or self.rank > 8 or self.rank == 0 or self.progress > 100 or self.progress < 0:
            raise ValueError
        if r == self.rank: 
            return 3
        if r < 0:
            if self.rank < 0:
                if abs(self.rank - r) == 1 and self.rank > r:
                    return 1
                if abs(self.rank - r) >= 2 and self.rank > r:
                    return 0
                else:
                    return 10 * abs(self.rank - r) * abs(self.rank - r)
            else:
                if abs(self.rank - r - 1) == 1 and self.rank > r:
                    return 1
                if abs(self.rank - r - 1) >= 2 and self.rank > r:
                    return 0
        else:
            if self.rank < 0:
                if abs(self.rank - r + 1) == 1 and self.rank > r:
                    return 1
                if abs(self.rank - r + 1) >= 2 and self.rank > r:
                    return 0
                else:
                    return 10 * abs(self.rank - r + 1) * abs(self.rank - r + 1)
            else:
                if abs(self.rank - r) == 1 and self.rank > r:
                    return 1
                if abs(self.rank - r) >= 2 and self.rank > r:
                    return 0
                else:
                    return 10 * abs(self.rank - r) * abs(self.rank - r)

    def inc_progress(self, r):
        print(r, self.rank, self.progress)
        prog = self.calc_progress(r)
        up = 0
        self.progress += prog
        if self.progress >= 100:
            while self.progress >= 100:
                self.progress -= 100
                up += 1
        if up != 0:
            if self.rank + up >= 8:
                self.rank, self.progress = 8, 0
            else:
                if self.rank < 0 and self.rank + up >= 0:
                    up += 1
                self.rank += up
        else:
            if self.rank >= 8:
                self.rank, self.progress = 8, 0
