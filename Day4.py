from collections import Counter

def main():
    lines = []
    with open('day4.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    part1 = 0
    for line in lines:
        tmp = line.split("-")
        name = ""
        for i in range(len(tmp) - 1):
            name += tmp[i]

        legitChecksum = tmp[-1][-6:-1]

        dict = Counter(name)
        checksum = ""
        for iter in range(5):
            maxNumber = 0
            maxValue = ""
            for i in sorted(dict):
                if dict[i] > maxNumber:
                    maxNumber = dict[i]
                    maxValue = i

            checksum += maxValue
            dict.pop(maxValue)

        if checksum == legitChecksum:
            sectorID = tmp[-1]
            for index, char in enumerate(sectorID):
                if char == "[":
                    sectorID = int(tmp[-1][0:index])
                    break
            part1 += sectorID

    print(f"Part 1: {part1}")

    for line in lines:
        tmp = line.split("-")
        name = ""
        for i in range(len(tmp) - 1):
            name += tmp[i]
            name += "-"

        OGsectorID = tmp[-1]
        for index, char in enumerate(OGsectorID):
            if char == "[":
                OGsectorID = int(tmp[-1][0:index])
                break

        sectorID = OGsectorID % 26

        newName = ""
        for char in name:
            if char == "-":
                newName += "-"
                continue
            newChar = chr(ord(char) + sectorID)
            if ord(newChar) >= 123:
                newChar = chr(ord(char) - (26 - sectorID))
            newName += newChar

        if "north" in newName:
            print(f"Part 2: {OGsectorID}")
            break








if __name__ == "__main__":
    main()