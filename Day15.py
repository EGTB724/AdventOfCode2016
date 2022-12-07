def main():
    lines = []
    with open('day15.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    discs = []

    for line in lines:
        words = line[0:-1].split()

        num = int(words[3])
        start = int(words[11])
        discs.append(Disk(num, start))

    startingTime = 0

    while True:
        scenarioGood = True
        simulationTime = startingTime
        for disc in discs:
            simulationTime += 1
            if ((disc.startingPosition + simulationTime) % disc.numPositions) == 0:
                continue
            else:
                scenarioGood = False

        if scenarioGood:
            break

        startingTime += 1

    print(f"Good Starting Time: {startingTime}")


class Disk:
    def __init__(self, numPositions, startingPosition):
        self.numPositions = numPositions
        self.startingPosition = startingPosition


if __name__ == "__main__":
    main()