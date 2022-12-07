def main():
    lines = []
    with open('day7.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    numSupported = 0
    for line in lines:
        inBracket = False
        goodString = False
        for i in range(0, len(line) - 3):
            if line[i] == "[":
                inBracket = True
                continue
            if line[i] == "]":
                inBracket = False
                continue

            if line[i] == line[i+3] and line[i+1] == line[i+2] and not line[i] == line[i+1]:
                if inBracket:
                    goodString = False
                    break
                if not inBracket:
                    goodString = True

        if goodString:
            numSupported += 1

    print(f"Part 1: {numSupported}")


    numSupported = 0
    for line in lines:
        inBracket = False
        list1 = []
        list2 = []
        for i in range(0, len(line) - 2):
            if line[i] == "[":
                inBracket = True
                continue
            if line[i] == "]":
                inBracket = False
                continue

            if line[i] == line[i+2] and not line[i] == line[i+1]:
                if inBracket:
                    list1.append(line[i:i+3])
                else:
                    list2.append(line[i:i + 3])

        if len(list1) == 0 or len(list2) == 0:
            continue

        stringCounted = False
        for j in list1:
            for k in list2:
                if j[0] == k[1] and k[0] == j[1]:
                    numSupported += 1
                    stringCounted = True
                    break
            if stringCounted:
                break

    print(f"Part 2: {numSupported}")

if __name__ == "__main__":
    main()