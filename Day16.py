def main():
    input = "10111100110001111"
    desiredLength = 35651584

    while len(input) < desiredLength:
        copy = input
        copy = copy[::-1]

        reverseCopy = ""
        for char in copy:
            if char == "1":
                reverseCopy += "0"
            else:
                reverseCopy += "1"

        input = input + "0" + reverseCopy

    input = input[:desiredLength]
    checksum = ""

    while len(checksum) % 2 == 0:
        checksum = ""
        for index in range(0, len(input), 2):
            if input[index] == input[index + 1]:
                checksum += "1"
            else:
                checksum += "0"

        input = checksum

    print(checksum)


if __name__ == "__main__":
    main()