def main():
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    grid = []
    total = 0
    with open("./2025/inputs/input4.txt") as f:
        for line in f:
            elements = line.strip()
            grid.append(elements)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '@':
                continue
            count = 0
            for direction in directions:
                x = i + direction[0]
                y = j + direction[1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[i]):
                    if grid[x][y] == '@':
                        count += 1
            if count < 4:
                total += 1
                
    print(total)

if __name__ == "__main__":
    main()