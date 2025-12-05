def main():
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    grid = []
    final_total = 0
    tp_available = True
    with open("./2025/4/input.txt") as f:
        for line in f:
            elements = line.strip()
            grid.append(list(elements))
    while(tp_available):
        total = 0        
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
                    grid[i][j] = '.'
                    total += 1
        if total == 0:
            tp_available = False
        else:
            final_total += total
    print(final_total)

if __name__ == "__main__":
    main()