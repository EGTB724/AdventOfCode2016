def main():
    lines = []
    with open('day10.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    bots = [[-1 for x in range(2)] for y in range(1000)]

    visited = [0] * len(lines)
    outputBins = [-1] * 100

    part1 = 0

    while 0 in visited:
        for index, line in enumerate(lines):
            if visited[index] == 0:
                words = line.split()
                if words[0] == "bot":
                    botNumber = int(words[1])

                    bot = bots[botNumber]
                    if bot[0] == -1 or bot[1] == -1:
                        continue

                    typeOne = words[5]
                    numOne = int(words[6])
                    typeTwo = words[10]
                    numTwo = int(words[11])

                    lowNum = min(bot[0], bot[1])
                    highNum = max(bot[0], bot[1])

                    if lowNum == 17 and highNum == 61:
                        part1 = botNumber

                    if typeOne == "bot":
                        if bots[numOne][0] == -1:
                            bots[numOne][0] = lowNum
                        else:
                            bots[numOne][1] = lowNum


                    elif typeOne == "output":
                        #print(f"{lowNum} goes to output bin {numOne}")
                        outputBins[numOne] = lowNum

                    if typeTwo == "bot":
                        if bots[numTwo][0] == -1:
                            bots[numTwo][0] = highNum
                        else:
                            bots[numTwo][1] = highNum

                    elif typeTwo == "output":
                        #print(f"{highNum} goes to output bin {numTwo}")
                        outputBins[numTwo] = highNum

                    #print(f"Completed line {index + 1}")
                    visited[index] = 1

                elif words[0] == "value":
                    num = int(words[1])
                    botNumber = int(words[5])

                    if bots[botNumber][0] == -1:
                        bots[botNumber][0] = num
                    else:
                        bots[botNumber][1] = num

                    #print(f"Completed line {index + 1}")
                    visited[index] = 1


    print(f"Part 1: {part1}")
    print(f"Part 2: {outputBins[0] * outputBins[1] * outputBins[2]}")
if __name__ == "__main__":
    main()