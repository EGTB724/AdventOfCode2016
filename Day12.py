def main():
    lines = []
    with open('day12.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    registers = {"a": 0, "b": 0, "c": 1, "d": 0}
    numInstructions = len(lines)

    currentInstruction = 0
    while currentInstruction < numInstructions:
        instruction = lines[currentInstruction].split()
        command = instruction[0]

        if command == "cpy":
            if instruction[1].isnumeric():
                registers[instruction[2]] = int(instruction[1])
            else:
                registers[instruction[2]] = registers[instruction[1]]

        elif command == "inc":
            registers[instruction[1]] = registers[instruction[1]] + 1

        elif command == "dec":
            registers[instruction[1]] = registers[instruction[1]] - 1

        elif command == "jnz":
            if instruction[1].isnumeric():
                if int(instruction[1]) != 0:
                    currentInstruction += int(instruction[2]) - 1
            else:
                if registers[instruction[1]] != 0:
                    currentInstruction += int(instruction[2]) - 1

        currentInstruction += 1

    print(registers)
    print("done")


if __name__ == "__main__":
    main()