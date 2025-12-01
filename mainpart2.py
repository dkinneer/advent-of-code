import math

def main():
    pos = 50
    prevPos = 50
    zeroCount = 0
    with open("./2025/1/input.txt") as f:
        for line in f:
            dirChar = line[:1]
            nums = int(line[1:])

            if dirChar == "L":
                pos -= nums
                zeroCount += math.floor((abs(prevPos - pos) + (100 - (prevPos % 100))) / 100)
                pos = (pos % 100 + 100) % 100
            else:
                pos += nums
                zeroCount += math.floor((abs(prevPos - pos) - (prevPos % 100)) / 100)
                pos = pos % 100

            prevPos = pos
    print(zeroCount)

main()