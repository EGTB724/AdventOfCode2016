def main():
    lines = []
    with open('day23.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    registers = {"a": 12, "b": 0, "c": 0, "d": 0}
    numInstructions = len(lines)

    currentInstruction = 0
    while currentInstruction < numInstructions:
        print(currentInstruction, lines[currentInstruction])
        instruction = lines[currentInstruction].split()
        command = instruction[0]

        if command == "cpy":
            if not instruction[2].lstrip('-').isnumeric():
                if instruction[1].lstrip('-').isnumeric():
                    registers[instruction[2]] = int(instruction[1])
                else:
                    registers[instruction[2]] = registers[instruction[1]]

        elif command == "inc":
            if not instruction[1].lstrip('-').isnumeric():
                registers[instruction[1]] = registers[instruction[1]] + 1

        elif command == "dec":
            if not instruction[1].lstrip('-').isnumeric():
                registers[instruction[1]] = registers[instruction[1]] - 1

        elif command == "jnz":
            if instruction[1].lstrip('-').isnumeric():
                if int(instruction[1]) != 0:
                    if instruction[2].lstrip('-').isnumeric():
                        currentInstruction += int(instruction[2]) - 1
                    else:
                        currentInstruction += registers[instruction[2]] - 1
            else:
                if registers[instruction[1]] != 0:
                    if instruction[2].lstrip('-').isnumeric():
                        currentInstruction += int(instruction[2]) - 1
                    else:
                        currentInstruction += registers[instruction[2]] - 1

        elif command == "tgl":
            if instruction[1].lstrip('-').isnumeric():
                offset = int(instruction[1])
            else:
                offset = registers[instruction[1]]

            if currentInstruction + offset < numInstructions:
                offset_instruction = lines[currentInstruction + offset]
                offset_instruction = offset_instruction.split()

                if offset_instruction[0] == "inc":
                    offset_instruction[0] = "dec"
                elif offset_instruction[0] == "dec":
                    offset_instruction[0] = "inc"
                elif offset_instruction[0] == "tgl":
                    offset_instruction[0] = "inc"
                elif offset_instruction[0] == "jnz":
                    offset_instruction[0] = "cpy"
                elif offset_instruction[0] == "cpy":
                    offset_instruction[0] = "jnz"

                instruction_string = ""
                for ins_split in offset_instruction:
                    instruction_string += ins_split
                    instruction_string += " "

                lines[currentInstruction + offset] = instruction_string[:-1]

        elif command == "special1":
            registers['a'] = registers['a'] + (registers['b'] * registers['d'])
            registers['d'] = 0
            registers['c'] = 0

        currentInstruction += 1

    print(registers)


if __name__ == "__main__":
    main()