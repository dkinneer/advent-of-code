def main():
    total = 0
    with open("./2025/inputs/input2.txt") as f:
        line = f.readline()
    ranges = line.split(",")
    for i in ranges:
        nums = i.split("-")
        large = int(nums[1])
        small = int(nums[0])
        for k in range(small, large):
            s = str(k)
            if s[:len(s)//2 + len(s)%2] == s[len(s)//2 + len(s)%2:]:
                total += k

    print(total)

main()