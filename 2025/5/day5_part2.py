from itertools import chain

def main():
    ranges = []
    merged = []
    count = 0
    with open("./2025/inputs/input5.txt") as f:
        for line in f:
            if "-" in line:
                ranges.append([int(num) for num in line.strip().split('-')])

        ranges.sort(key=lambda r: r[0])
        
        for start, end in ranges:
            if merged == [] or merged[-1][1] < start:
                merged.append([start, end])
            elif merged[-1][1] < end:
                merged[-1][1] = end

        for start, end in merged:
            count += end - start + 1

        print(count)

if __name__ == "__main__":
    main()
