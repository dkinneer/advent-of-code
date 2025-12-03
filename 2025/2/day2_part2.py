import re

class Solver:
    def solve(self, ranges):
        total = 0
        for i in ranges:
            nums = i.split("-")
            large = int(nums[1])
            small = int(nums[0])
            for k in range(small, large + 1):
                s = str(k)
                for j in range(1, (len(s) // 2) + 1):
                    if self.checkPattern(s[:j], s):
                        total += k
                        break
        return total
    
    def checkPattern(self, pattern, string):
        return re.fullmatch(f"({pattern})+", string) is not None

def main():
    solver = Solver()
    with open("./2025/2/input.txt") as f:
        line = f.readline()
    ranges = line.split(",")
    print(solver.solve(ranges))

if __name__ == "__main__":
    main()