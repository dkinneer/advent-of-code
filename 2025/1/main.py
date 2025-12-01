def main():
    pos = 50
    zeroCount = 0
    with open("./2025/1/input.txt") as f:
        for line in f:
            dirChar = line[:1]
            nums = int(line[1:])
            if dirChar == "L":
                pos -= nums
                pos = (pos % 100 + 100) % 100
            else:
                pos += nums
                pos = pos % 100

            if pos == 0:
                zeroCount += 1
    print(zeroCount)

main()