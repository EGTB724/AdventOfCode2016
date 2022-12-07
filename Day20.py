ranges = None

def main():
    lines = []
    with open('day20.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    range_list = []
    for line in lines:
        line_split = line.split('-')
        range_list.append((int(line_split[0]), int(line_split[1])))
    global ranges
    ranges = range_list

    value = 0
    good_values = 0
    while True:
        if value >= 2**32 - 1:
            break

        in_range, high_value = in_a_range(value)
        if not in_range:
            # print(value)
            value += 1
            good_values += 1
        else:
            value = high_value + 1

    print(good_values)


def in_a_range(value):
    global ranges

    for range in ranges:
        if range[0] <= value <= range[1]:
            return True, range[1]

    return False, 0


if __name__ == "__main__":
    main()