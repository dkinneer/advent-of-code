class Solver:
    def solve(self, ranges):
        total = 0
        for i in ranges:
            print(ranges)
            nums = i.split("-")
            large = int(nums[1])
            small = int(nums[0])
            for k in range(small, large + 1):
                s = str(k)
                for j in range(1, (len(s) // 2) + 1):
                    if self.checkPattern(s[:j], s):
                        total += k
        return total
    
    def checkPattern(self, pattern, string):
        patternLength = len(pattern)
        stringLength =  len(string)
        if stringLength % patternLength != 0:
            return False
        for i in range(patternLength, (stringLength // patternLength)):
            start = i * patternLength
            if string[start:(start + patternLength)] != pattern:
                return False
        return True

def main():
    solver = Solver()
    with open("./2025/2/input.txt") as f:
        line = f.readline()
    ranges = line.split(",")
    print(solver.solve(ranges))

if __name__ == "__main__":
    main()