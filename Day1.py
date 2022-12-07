import math

def main():
    lines = []
    with open('day1.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    instructions = lines[0].split(",")
    instructions = [s.strip() for s in instructions]

    #Directions
    #0 - up
    #1- right
    #2 - down
    #3 - left

    #L: ((direction + 4) - 1) % 4
    #R: (direction + 1) % 4

    direction = 0
    xPos = 0
    yPos = 0
    for instruction in instructions:
        rotation = instruction[0]
        magnitude = int(instruction[1:])

        if rotation == "L":
            direction = ((direction + 4) - 1) % 4
        else:
            direction = (direction + 1) % 4

        if direction == 0:
            yPos += magnitude
        if direction == 1:
            xPos += magnitude
        if direction == 2:
            yPos -= magnitude
        if direction == 3:
            xPos -= magnitude

    print(f"Part 1: {abs(xPos) + abs(yPos)}")

    direction = 0
    xPos = 0
    yPos = 0
    part2 = 0
    positions = []
    positions.append((xPos, yPos))
    for instruction in instructions:
        rotation = instruction[0]
        magnitude = int(instruction[1:])

        if rotation == "L":
            direction = ((direction + 4) - 1) % 4
        else:
            direction = (direction + 1) % 4

        if direction == 0:
            for i in range(1, magnitude + 1):
                yPos += 1
                positions.append((xPos,yPos))
        if direction == 1:
            for i in range(1, magnitude + 1):
                xPos += 1
                positions.append((xPos,yPos))
        if direction == 2:
            for i in range(1, magnitude + 1):
                yPos -= 1
                positions.append((xPos,yPos))
        if direction == 3:
            for i in range(1, magnitude + 1):
                xPos -= 1
                positions.append((xPos,yPos))

        res = list(set([ele for ele in positions
                        if positions.count(ele) > 1]))
        if len(res) >= 1:
            part2 = abs(res[0][0]) + abs(res[0][1])
            break

    print(f"Part 2: {part2}")

if __name__ == "__main__":
    main()