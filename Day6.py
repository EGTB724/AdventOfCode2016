from collections import Counter

def main():
    lines = []
    with open('temp.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    length = len(lines[0])
    part1 = ""
    for i in range(length):
        string = ""
        for line in lines:
               string += line[i]

        dict = Counter(string)
        part1 += max(dict, key=dict.get)

    print(f"Part 1: {part1}")

    part2 = ""
    for i in range(length):
        string = ""
        for line in lines:
            string += line[i]

        dict = Counter(string)
        part2 += min(dict, key=dict.get)

    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()