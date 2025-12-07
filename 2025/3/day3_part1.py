class Solver:
    def solve(self, line):
        biggest = 0
        big = 0
        for i in line:
            num = int(i)
            if big > biggest:
                biggest = big
                big = 0
            if num > big:
                big = num
        return (biggest * 10) + big

def main():
    solver = Solver()
    total = 0
    with open("./2025/inputs/input3.txt") as f:
        for line in f:
            total += solver.solve(line.strip())
    print(total)

if __name__ == "__main__":
    main()