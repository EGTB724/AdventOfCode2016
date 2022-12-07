def main():
    lines = []
    with open('day3.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    numValid = 0
    for line in lines:
        sides = line.split()
        side1 = int(sides[0])
        side2 = int(sides[1])
        side3 = int(sides[2])

        if side1 + side2 <= side3:
            continue
        if side2 + side3 <= side1:
            continue
        if side3 + side1 <= side2:
            continue

        numValid += 1

    print(f"Part 1: {numValid}")

    triangles = []
    a = []
    b = []
    c = []
    for line in lines:
        sides = line.split()
        a.append(int(sides[0]))
        b.append(int(sides[1]))
        c.append(int(sides[2]))

        if len(a) == 3:
            triangles.append(a)
            triangles.append(b)
            triangles.append(c)
            a = []
            b = []
            c = []

    numValid = 0
    for triangle in triangles:
        side1 = triangle[0]
        side2 = triangle[1]
        side3 = triangle[2]

        if side1 + side2 <= side3:
            continue
        if side2 + side3 <= side1:
            continue
        if side3 + side1 <= side2:
            continue

        numValid += 1

    print(f"Part 2: {numValid}")

if __name__ == "__main__":
    main()