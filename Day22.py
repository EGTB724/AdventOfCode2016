def main():
    lines = []
    with open('day22.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    # Delete the first two lines
    del lines[0:2]

    # Store everything in a 2D array
    NUM_ROWS = 37
    NUM_COLS = 25
    grid = [[None for i in range(NUM_COLS)] for j in range(NUM_ROWS)]
    for line in lines:
        line_split = line.split()
        size = int(line_split[1][:-1])
        used = int(line_split[2][:-1])
        available = int(line_split[3][:-1])
        percent_used = int(line_split[4][:-1])

        name_break  = line_split[0].split('-')
        row = int(name_break[1][1:])
        col = int(name_break[2][1:])

        grid[row][col] = Node(size, used, available, percent_used)

    # Find all viable pairs
    viable_pairs = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            for k in range(NUM_ROWS):
                for l in range(NUM_COLS):
                    if i == k and j == l:
                        continue

                    node_A = grid[i][j]
                    node_B = grid[k][l]

                    if is_viable(node_A, node_B):
                        viable_pairs += 1


    print("Part 1:", viable_pairs)

    # Part 2 was done by hand
    # I just printed the graph as was done in the example, and then moved things around
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if i == NUM_ROWS - 1 and j == 0:
                print('G', end='')
            elif i == 0 and j == 0:
                print('@', end='')
            elif grid[i][j].size >= 100 and grid[i][j].percent_used >=80:
                print("#", end='')
            elif grid[i][j].used == 0:
                print('_', end='')
            else:
                print('.', end='')
            print(' ', end='')
        print()


def is_viable(node_A, node_B):
    if node_A.used == 0:
        return False

    if node_A.used <= node_B.available:
        return True

    return False


class Node:
    def __init__(self, size, used, available, percent_used):
        self.size = size
        self.used = used
        self.available = available
        self.percent_used = percent_used
        self.goal_data = False


if __name__ == "__main__":
    main()