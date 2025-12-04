class Solver:
    def solve(self, line):
        nums = list(map(int, line))
        stack = [nums[0]]
        for i, val in enumerate(nums[1:]):
            if len(stack) + len(nums[i+1:]) == 12:
                stack.extend(nums[i+1:])
                break
            elif stack[-1] < val:
                while len(stack) + len(nums[i+1:]) > 12 and len(stack) != 0:
                    if stack[-1] >= val:
                        break
                    else:
                        stack.pop()
                stack.append(val)
            elif len(stack) < 12:
                stack.append(val)
        return int(''.join(map(str, stack)))

def main():
    solver = Solver()
    total = 0
    with open("./2025/3/input.txt") as f:
        for line in f:
            total += solver.solve(line.strip())
    print(total)

if __name__ == "__main__":
    main()