def main():
    lines = []
    with open('day2.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]


    combo = ""
    number = 5
    for line in lines:
        for char in line:
            if char == "U":
                if number >= 4:
                    number -= 3
            elif char == "D":
                if number <= 6:
                    number += 3
            elif char == "L":
                if number == 1 or number == 4 or number == 7:
                    continue
                else:
                    number -= 1
            elif char == "R":
                if number == 3 or number == 6 or number == 9:
                    continue
                else:
                    number += 1
        combo += str(number)

    print(f"Part 1: {combo}")


    grid = []
    grid.append([".", ".", "1", ".", "."])
    grid.append([".", "2", "3", "4", "."])
    grid.append(["5", "6", "7", "8", "9"])
    grid.append([".", "A", "B", "C", "."])
    grid.append([".", ".", "D", ".", "."])

    row = 2
    col = 0
    combo = ""
    for line in lines:
        for char in line:
            if char == "U":
                if row == 0:
                    continue
                if grid[row-1][col] == ".":
                    continue
                row -= 1
            elif char == "D":
                if row == len(grid) - 1:
                    continue
                if grid[row+1][col] == ".":
                    continue
                row += 1
            elif char == "L":
                if col == 0:
                    continue
                if grid[row][col-1] == ".":
                    continue
                col -= 1
            elif char == "R":
                if col == len(grid[row]) - 1:
                    continue
                if grid[row][col+1] == ".":
                    continue
                col += 1
        combo += grid[row][col]

    print(f"Part 2: {combo}")

if __name__ == "__main__":
    main()