from itertools import permutations

def main():
    lines = []
    with open('day21.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    # Input string from website
    input_string = "abcdefgh"

    # Parse through all of the instructions
    for line in lines:
        line_split = line.split()

        if line_split[0] == "swap":
            if line_split[1] == "position":
                input_string = swap_position(input_string, int(line_split[2]), int(line_split[5]))
            if line_split[1] == "letter":
                input_string = swap_letter(input_string, line_split[2], line_split[5])

        if line_split[0] == "rotate":
            if line_split[1] == "left":
                input_string = rotate_left(input_string, int(line_split[2]))
            if line_split[1] == "right":
                input_string = rotate_right(input_string, int(line_split[2]))
            if line_split[1] == "based":
                input_string = rotate_on_letter_position(input_string, line_split[6])

        if line_split[0] == "reverse":
            input_string = reverse(input_string, int(line_split[2]), int(line_split[4]))

        if line_split[0] == "move":
            input_string = move(input_string, int(line_split[2]), int(line_split[5]))

    print("Part 1:", input_string)


    desired_output = "fbgdceah"
    input_list = [''.join(p) for p in permutations('abcdefgh')]

    for input_string in input_list:
        string_copy = input_string

        for line in lines:
            line_split = line.split()

            if line_split[0] == "swap":
                if line_split[1] == "position":
                    input_string = swap_position(input_string, int(line_split[2]), int(line_split[5]))
                if line_split[1] == "letter":
                    input_string = swap_letter(input_string, line_split[2], line_split[5])

            if line_split[0] == "rotate":
                if line_split[1] == "left":
                    input_string = rotate_left(input_string, int(line_split[2]))
                if line_split[1] == "right":
                    input_string = rotate_right(input_string, int(line_split[2]))
                if line_split[1] == "based":
                    input_string = rotate_on_letter_position(input_string, line_split[6])

            if line_split[0] == "reverse":
                input_string = reverse(input_string, int(line_split[2]), int(line_split[4]))

            if line_split[0] == "move":
                input_string = move(input_string, int(line_split[2]), int(line_split[5]))

        if input_string == desired_output:
            print("Part 2:", string_copy)


def swap_position(input_string, x, y):
    input_as_list = list(input_string)
    input_as_list[x], input_as_list[y] = input_as_list[y], input_as_list[x]
    input_string = ''.join(input_as_list)
    return input_string


def swap_letter(input_string, x, y):
    index_1 = input_string.rfind(x)
    index_2 = input_string.rfind(y)
    return swap_position(input_string, index_1, index_2)


def rotate_left(input_string, steps):
    for i in range(steps):
        input_string = input_string[1:] + input_string[0]
    return input_string


def rotate_right(input_string, steps):
    for i in range(steps):
        input_string = input_string[-1] + input_string[:-1]
    return input_string


def rotate_on_letter_position(input_string, letter):
    index = input_string.rfind(letter)
    if index >= 4:
        index += 1
    index += 1
    return rotate_right(input_string, index)


def reverse(input_string, x, y):
    reverse_string = input_string[x:y+1]
    reverse_string = reverse_string[::-1]
    input_string = input_string[:x] + reverse_string + input_string[y+1:]
    return input_string


def move(input_string, x, y):
    input_as_list = list(input_string)
    popped_val = input_as_list[x]
    input_as_list.pop(x)
    input_as_list.insert(y, popped_val)
    input_string = ''.join(input_as_list)
    return input_string


if __name__ == "__main__":
    main()