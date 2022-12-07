def main():
    lines = []
    with open('day25.txt') as f:
        lines = f.readlines()

    lines = [s.strip() for s in lines]

    a_value = 0
    while True:
        registers = {"a": a_value, "b": 0, "c": 0, "d": 0}
        numInstructions = len(lines)

        currentInstruction = 0
        clock_array = []
        clock_is_good = True
        while len(clock_array) < 100:
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

            elif command == "out":
                if instruction[1].lstrip('-').isnumeric():
                    if len(clock_array) % 2 == 0:
                        if int(instruction[1]) == 1:
                            clock_array.append(int(instruction[1]))
                        else:
                            print(f"{a_value} is bad")
                            break
                    else:
                        if int(instruction[1]) == 0:
                            clock_array.append(int(instruction[1]))
                        else:
                            print(f"{a_value} is bad")
                            break
                else:
                    if len(clock_array) % 2 == 0:
                        if registers[instruction[1]] == 0:
                            clock_array.append(registers[instruction[1]])
                        else:
                            print(f"{a_value} is bad")
                            clock_is_good = False
                            break
                    else:
                        if registers[instruction[1]] == 1:
                            clock_array.append(registers[instruction[1]])
                        else:
                            print(f"{a_value} is bad")
                            clock_is_good = False
                            break

            currentInstruction += 1

        #Check if the clock is good
        if clock_is_good:
            print(f"a = {a_value}: clock is {clock_array}")
            break

        a_value += 1




if __name__ == "__main__":
    main()