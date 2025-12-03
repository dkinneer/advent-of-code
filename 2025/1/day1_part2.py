import math

class Solver:

    def __init__(self, pos):
        self.pos = pos
        self.prevPos = pos
    
    def get_between_zeros(self, line):
        dirChar = line[:1]
        nums = int(line[1:])

        if dirChar == "L":
            self.pos -= nums
            zeros = math.floor((abs(self.prevPos - self.pos) + ((100 - (self.prevPos % 100)) % 100)) / 100)
        else:
            self.pos += nums
            zeros = math.floor((abs(self.prevPos - self.pos) + ((100 + (self.prevPos % 100)) % 100)) / 100)
        self.prevPos = self.pos
        return zeros
    
def main():
    zeroCount = 0
    solver = Solver(50)
    with open("./2025/1/input.txt") as f:
        for line in f:
            zeroCount += solver.get_between_zeros(line)

    print(zeroCount)

main()