import hashlib

def main():
    inputString = "jlmsuwbz"
    index = 0

    hashes = []
    validIndices = []

    while True:
        result = ""
        if len(hashes) > index:
            result = hashes[index]
        else:
            md5String = inputString + str(index)

            for i in range(0, 2017):
                result = hashlib.md5(md5String.encode()).hexdigest()
                md5String = result

            hashes.append(result)

        resultExamined = False

        for r_index, char in enumerate(result):
            if r_index == len(result) - 2:
                break

            if resultExamined:
                break

            if result[r_index] == result[r_index + 1] and result[r_index] == result[r_index + 2]:
                print(f"examining {result} at index {index} on character {result[r_index]}")
                resultExamined = True
                letter = result[r_index]
                matchFound = False


                for inner_index in range(index+1, index+1001):
                    if matchFound:
                        break

                    newResult = ""

                    if len(hashes) > inner_index:
                        newResult = hashes[inner_index]
                    else:
                        newMd5String = inputString + str(inner_index)

                        for i in range(0, 2017):
                            newResult = hashlib.md5(newMd5String.encode()).hexdigest()
                            newMd5String = newResult

                        hashes.append(newResult)

                    for newIndex, newChar in enumerate(newResult):
                        if newIndex == len(newResult) - 4:
                            break

                        if newResult[newIndex] == newResult[newIndex + 1] and newResult[newIndex] == newResult[newIndex + 2] and newResult[newIndex] == newResult[newIndex + 3] and newResult[newIndex] == newResult[newIndex + 4] and newResult[newIndex] == letter:
                            print(f"    {index} has a match at {inner_index}: {result} and {newResult}")
                            if index not in validIndices:
                                validIndices.append(index)
                            matchFound = True
                            break

                if not matchFound:
                    print(f"    {index} does not have a match")

        if len(validIndices) == 64:
            break

        index += 1

    print("Found all matches")



if __name__ == "__main__":
    main()