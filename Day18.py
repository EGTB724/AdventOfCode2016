def main():
    lines = []
    with open('day18.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    line = lines[0]

    num_rows = 400000
    num_cols = len(line)

    grid = [["" for i in range(num_cols)] for j in range(num_rows)]

    for i in range(num_cols):
        grid[0][i] = line[i]

    for row_index in range(1, num_rows):
        for col_index in range(num_cols):
            upper_left = grid[row_index - 1][col_index - 1] if col_index != 0 else "."
            upper = grid[row_index - 1][col_index]
            upper_right = grid[row_index - 1][col_index + 1] if col_index != num_cols - 1 else "."

            curr_value = "."
            if upper_left == "^" and upper == "^" and upper_right == ".":
                curr_value = "^"
            elif upper_left == "." and upper == "^" and upper_right == "^":
                curr_value = "^"
            elif upper_left == "^" and upper == "." and upper_right == ".":
                curr_value = "^"
            elif upper_left == "." and upper == "." and upper_right == "^":
                curr_value = "^"

            grid[row_index][col_index] = curr_value

    num_safe_tiles = 0
    for row_index in range(num_rows):
        for col_index in range(num_cols):
            if grid[row_index][col_index] == ".":
                num_safe_tiles += 1

    print(num_safe_tiles)


if __name__ == "__main__":
    main()