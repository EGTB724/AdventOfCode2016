import numpy as np

def main():
    lines = []
    with open('day8.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    grid = np.zeros((6,50), np.int_)

    for line in lines:
        tmp = line.split()

        if tmp[0] == "rect":
            width = int(tmp[1].split("x")[0])
            height = int(tmp[1].split("x")[1])

            grid[0:height,0:width] = 1

        elif tmp[0] == "rotate":
            if tmp[1] == "row":
                row = int(tmp[2].split("=")[1])
                amount = int(tmp[4])

                grid[row, :] = np.roll(grid[row, :], amount, 0)

            elif tmp[1] == "column":
                col = int(tmp[2].split("=")[1])
                amount = int(tmp[4])

                grid[:, col] = np.roll(grid[:, col], amount, 0)

    print(f"Part 1: {np.count_nonzero(grid)}")
    print("Part 2: See text below")
    for i in range(6):
        for j in range(50):
            if grid[i,j] == 1:
                print("# ", end="")
            else:
                print("  ", end="")
        print()


if __name__ == "__main__":
    main()