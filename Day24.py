import itertools
import math

def main():
    lines = []
    with open('day24.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    # Make the grid
    NUM_ROWS = len(lines)
    NUM_COLS = len(lines[0])
    number_dict = {}
    grid = [['' for j in range(NUM_COLS)] for i in range(NUM_ROWS)]
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            grid[i][j] = lines[i][j]

            if lines[i][j] != "#" and lines[i][j] != ".":
                number_dict[lines[i][j]] = (i, j)

    # Do a BFS starting from every number
    distance_grid = [[0 for j in range(len(number_dict))] for i in range(len(number_dict))]
    for key in number_dict:
        value = int(key)
        start_row = int(number_dict[key][0])
        start_col = int(number_dict[key][1])

        queue = []
        discovered = []

        queue.append((start_row, start_col, 0))
        discovered.append((start_row, start_col))

        while queue:
            # Pop it
            curr_row, curr_col, distance = queue.pop(0)

            # See if we've found a number or not
            if grid[curr_row][curr_col] != "#" and grid[curr_row][curr_col] != ".":
                # print(f"{value} has found {grid[curr_row][curr_col]} in {distance} steps")
                distance_grid[value][int(grid[curr_row][curr_col])] = int(distance)

            # Explore
            # Check if we can go left
            if curr_col > 0 and grid[curr_row][curr_col - 1] != "#" and (curr_row, curr_col - 1) not in discovered:
                queue.append((curr_row, curr_col - 1, distance + 1))
                discovered.append((curr_row, curr_col - 1))

            # Check if we can go up
            if curr_row > 0 and grid[curr_row - 1][curr_col] != "#" and (curr_row - 1, curr_col) not in discovered:
                queue.append((curr_row - 1, curr_col, distance + 1))
                discovered.append((curr_row - 1, curr_col))

            # Check if we can go right
            if curr_col < NUM_COLS - 1 and grid[curr_row][curr_col + 1] != "#" and (curr_row, curr_col + 1) not in discovered:
                queue.append((curr_row, curr_col + 1, distance + 1))
                discovered.append((curr_row, curr_col + 1))

            # Check if we can go down
            if curr_row < NUM_ROWS - 1 and grid[curr_row + 1][curr_col] != "#" and (curr_row + 1, curr_col) not in discovered:
                queue.append((curr_row + 1,curr_col, distance + 1))
                discovered.append((curr_row + 1, curr_col))

    # Perform a traveling salesman on the distance grid
    unique_nums = [i + 1 for i in range(len(number_dict) - 1)]
    perms = list(itertools.permutations(unique_nums))
    best_sum = math.inf
    best_path = None
    for perm in perms:
        path_perm = [0] + list(perm)
        curr_sum = 0
        for i in range(1, len(path_perm)):
            curr_sum += distance_grid[path_perm[i-1]][path_perm[i]]

        if curr_sum < best_sum:
            best_sum = curr_sum
            best_path = path_perm

    print("Part 1:", best_sum, best_path)

    # Perform a traveling salesman on the distance grid
    unique_nums = [i + 1 for i in range(len(number_dict) - 1)]
    perms = list(itertools.permutations(unique_nums))
    best_sum = math.inf
    best_path = None
    for perm in perms:
        path_perm = [0] + list(perm) + [0]
        curr_sum = 0
        for i in range(1, len(path_perm)):
            curr_sum += distance_grid[path_perm[i-1]][path_perm[i]]

        if curr_sum < best_sum:
            best_sum = curr_sum
            best_path = path_perm

    print("Part 2:", best_sum, best_path)


if __name__ == "__main__":
    main()