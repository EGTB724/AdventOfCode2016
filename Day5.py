import hashlib

def main():
    inputString = "reyedfim"

    index = 0
    password = ""
    for i in range(8):
        while (True):
            md5String = inputString + str(index)
            result = hashlib.md5(md5String.encode()).hexdigest()

            if result[0:5] == "00000":
                password += result[5]
                index += 1
                break

            index += 1

    print(f"Part 1: {password}")

    index = 0
    password = [".",".",".",".",".",".",".","."]
    while "." in password:

        md5String = inputString + str(index)
        result = hashlib.md5(md5String.encode()).hexdigest()

        if result[0:5] == "00000":
            pwIndex = result[5]
            if pwIndex.isnumeric() and 0 <= int(pwIndex) <= 7:
                if password[int(pwIndex)] == ".":
                    password[int(pwIndex)] = result[6]


        index += 1

    password = "".join(password)
    print(f"Part 2: {password}")

if __name__ == "__main__":
    main()