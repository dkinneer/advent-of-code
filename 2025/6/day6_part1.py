def main():
    nums = []
    total_count = 0
    sign = ''

    with open("./2025/inputs/input6.txt") as f:
        for line in f:
            nums.append(list(line.strip().split()))

    for i in range(len(nums[0])):
        count = 0
        for k in reversed(range(len(nums))):
            if nums[k][i] == '+':
                sign = '+'
            elif nums[k][i] == '*':
                sign = '*'
            else:
                if sign == '+':
                    count += int(nums[k][i])
                if sign == '*':
                    count = int(nums[k][i]) if count == 0 else int(nums[k][i]) * count
        total_count += count

    print(total_count)

if __name__ == "__main__":
    main()