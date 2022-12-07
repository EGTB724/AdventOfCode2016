def main():
    lines = []
    with open('day9.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    line = lines[0]

    index = 0
    part1 = ""
    while index < len(line):
        if line[index] == "(":
            startIndex = index
            while not line[index] == ")":
                index += 1
            endIndex = index

            marker = line[startIndex + 1:endIndex]
            breakup = marker.split("x")

            length = int(breakup[0])
            quantity = int(breakup[1])

            substring = line[index + 1: index+length + 1]
            for i in range(quantity):
                part1 += substring

            index = index + length + 1

        else:
            part1 += line[index]
            index += 1

    print(f"Part 1: {len(part1)}")

    part2 = 0
    index = 0
    weights = [1] * len(line)

    while index < len(line):
        if line[index] == "(":
            start = index
            while not line[index] == ")":
                index += 1
            end = index

            marker = line[start + 1: end]
            breakup = marker.split("x")

            length = int(breakup[0])
            quantity = int(breakup[1])

            for i in range(end + 1, end + 1 + length):
                weights[i] *= quantity
            index += 1
        else:
            part2 += weights[index]
            index += 1

    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()