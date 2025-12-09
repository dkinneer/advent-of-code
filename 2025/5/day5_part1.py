def main():
    allowed_nums = []
    nums = []
    count = 0
    with open("./2025/inputs/input5.txt") as f:
        for line in f:
            if "-" in line:
                allowed_nums.append(line.strip().split('-'))
            elif line.strip() != '':
                nums.append(int(line.strip()))
    
    for num in nums:
        for allowed_num in allowed_nums:
            if int(allowed_num[0]) <= num <= int(allowed_num[1]):
                count += 1
                break
    print(count)

if __name__ == "__main__":
    main()