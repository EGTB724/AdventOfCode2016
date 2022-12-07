import hashlib

def main():
    input_string = "njfxhljp"
    row, max_row = 0, 3
    col, max_col = 0, 3

    queue = []
    paths = []
    queue.append((row, col, input_string))

    while queue:
        row, col, string_to_hash = queue.pop(0)

        if row == max_row and col == max_col:
            paths.append(string_to_hash[len(input_string):])
            continue

        result = hashlib.md5(string_to_hash.encode()).hexdigest()[0:4]

        up_open = True if result[0] in "bcdef" else False
        down_open = True if result[1] in "bcdef" else False
        left_open = True if result[2] in "bcdef" else False
        right_open = True if result[3] in "bcdef" else False

        if up_open and row != 0:
            queue.append((row - 1, col, string_to_hash + "U"))
        if down_open and row != max_row:
            queue.append((row + 1, col, string_to_hash + "D"))
        if left_open and col != 0:
            queue.append((row, col - 1, string_to_hash + "L"))
        if right_open and col != max_col:
            queue.append((row, col + 1, string_to_hash + "R"))

    print(paths[1])
    print(len(paths[-1]))

if __name__ == "__main__":
    main()