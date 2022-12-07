from itertools import combinations

def main():
    #Grid 1
    grid = list()
    grid.append(["","","","","","","","","","",""])
    grid.append(["","","","","","","","","","","TM"])
    grid.append(["","","","","","TG","RG","RM","CG","CM",""])
    grid.append(["E","SG","SM","PG","PM","","","","","",""])

    bfs(grid)

    #Grid 2
    grid = list()
    grid.append(["","","","","","","","","","","","","","",""])
    grid.append(["","","","","","","","","","","TM","","","",""])
    grid.append(["","","","","","TG","RG","RM","CG","CM","","","","",""])
    grid.append(["E","SG","SM","PG","PM","","","","","","","EG","EM","DG","DM"])

    bfs(grid)

def getString(grid):
    stateString = ""
    bigList = []
    pairedLetters = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "":
                continue
            elif grid[row][col] == "E":
                stateString += str(row)
            else:
                # item is non empty and not "E"
                letter = grid[row][col][0]
                if letter in pairedLetters:
                    bigList.append((min(row, pairedLetters[letter]), max(row, pairedLetters[letter])))
                else:
                    pairedLetters[letter] = row

    bigList.sort(key=lambda y : (y[0], y[1]))

    for item in bigList:
        stateString += str(item[0]) + str(item[1])

    return stateString

def isStateSuccess(state):
    grid = state.grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if row == 0:
                if grid[row][col] == "":
                    return False
            else:
                if grid[row][col] != "":
                    return False
    return True

def printSolution(state):
    while state.parent is not None:
        state.parent.next = state
        state = state.parent

    count = -1

    part = -1
    if len(state.grid[0]) == 11:
        part = 1
    if len(state.grid[0]) == 15:
        part = 2

    while state is not None:
        grid = state.grid
        count += 1
        # print("")
        # for row in range(len(grid)):
        #     for col in range(len(grid[0])):
        #         print(grid[row][col] + " ", end="")
        #     print("")
        state = state.next

    print(f"Part {part} Solution takes {count} steps")

def makeMove(current, elevatorLevel, move, item1, item2=-1):
    """
    :param current: current state
    :param elevatorLevel: row index of the elevator
    :param move: either "up" or "down"
    :param item1: column index of the first item
    :param item2: column index of the second item (if there is one)
    :return:
    """
    if elevatorLevel == 0 and move == "up":
        return ""
    if elevatorLevel == 3 and move == "down":
        return ""

    if move == "down":
        itemsBelow = 0
        for i in range(len(current.grid[0])):
            if current.grid[elevatorLevel + 1][i] != "":
                itemsBelow += 1
        if itemsBelow == 0:
            return ""

    newGrid = [["" for i in range(len(current.grid[0]))] for j in range(4)]

    for row in range(4):
        for col in range(len(current.grid[0])):
            newGrid[row][col] = current.grid[row][col]

    #If there are two items
    if item2 != -1:
        if move == "up":
            newGrid[elevatorLevel - 1][item1] = current.grid[elevatorLevel][item1]
            newGrid[elevatorLevel][item1] = ""

            newGrid[elevatorLevel - 1][item2] = current.grid[elevatorLevel][item2]
            newGrid[elevatorLevel][item2] = ""

            newGrid[elevatorLevel - 1][0] = current.grid[elevatorLevel][0]
            newGrid[elevatorLevel][0] = ""

        elif move == "down":
            newGrid[elevatorLevel + 1][item1] = current.grid[elevatorLevel][item1]
            newGrid[elevatorLevel][item1] = ""

            newGrid[elevatorLevel + 1][item2] = current.grid[elevatorLevel][item2]
            newGrid[elevatorLevel][item2] = ""

            newGrid[elevatorLevel + 1][0] = current.grid[elevatorLevel][0]
            newGrid[elevatorLevel][0] = ""

    #If there is only one item
    else:
        if move == "up":
            newGrid[elevatorLevel - 1][item1] = current.grid[elevatorLevel][item1]
            newGrid[elevatorLevel][item1] = ""

            newGrid[elevatorLevel - 1][0] = current.grid[elevatorLevel][0]
            newGrid[elevatorLevel][0] = ""

        elif move == "down":
            newGrid[elevatorLevel + 1][item1] = current.grid[elevatorLevel][item1]
            newGrid[elevatorLevel][item1] = ""

            newGrid[elevatorLevel + 1][0] = current.grid[elevatorLevel][0]
            newGrid[elevatorLevel][0] = ""

    return newGrid


def isLegal(grid):
    for row in range(4):
        rowGenerators = []
        rowMicros = []
        for col in range(len(grid[0])):
            if grid[row][col] != "E" and grid[row][col] != "":
                if grid[row][col][1] == "G":
                    rowGenerators.append(grid[row][col][0])
                if grid[row][col][1] == "M":
                    rowMicros.append(grid[row][col][0])

        # In other words, if a chip is ever left in the same area as another RTG,
        # and it's not connected to its own RTG, the chip will be fried.
        unpairedM = 0

        for item in rowMicros:
            if item not in rowGenerators:
                unpairedM += 1

        if len(rowGenerators) > 0 and unpairedM > 0:
            return False

    return True


def bfs(grid):
    #Move set
    move = ["up", "down"]

    #We need an open stack
    openSet = []

    #We need a close set
    closeSet = {""}
    closeSet.remove("")


    start = state(grid)
    openSet.append(start)
    closeSet.add(getString(start.grid))

    success = False
    nodesExamined = 0

    while len(openSet) != 0 and not success:
        current = openSet.pop(0)
        if isStateSuccess(current):
            printSolution(current)
            # print(f"Nodes examined: {nodesExamined}")
            success = True
        else:
            #printState(current.grid)
            #find which level elevator is on
            elevatorLevel = -1
            for i in range(4):
                if current.grid[i][0] == "E":
                    elevatorLevel = i

            #make every subset of length 1 and 2 of items on that floor
            items = {""}
            items.remove("")
            for i in range(1, len(grid[0])):
                if current.grid[elevatorLevel][i] != "":
                    items.add(i)
            one = combinations(items, 1)
            two = combinations(items, 2)
            bigList = list(two) + list(one)

            #simulate moving those items up and down (including elevator)
            for tmp in bigList:
                for i in range(2):
                    succGrid = []

                    if len(tmp) == 2:
                        succGrid = makeMove(current, elevatorLevel, move[i], tmp[0], tmp[1])
                    else:
                        succGrid = makeMove(current, elevatorLevel, move[i], tmp[0])


                    #Check if state is legal, if not, terminate path
                    if succGrid == "":
                        continue

                    if not isLegal(succGrid):
                        continue

                    #get state string of new state
                    succString = getString(succGrid)

                    #If state hasnt been explored (by checking close), add stateString to close and state to open
                    if succString not in closeSet:
                        succState = state(succGrid, current)
                        closeSet.add(succString)
                        openSet.append(succState)

                        #Increment nodes explored
                        nodesExamined += 1

    if not success:
        print("No solution found")

class state:
    def __init__(self, grid, parent=None, next=None):
        self.grid = grid
        self.parent = parent
        self.next = next

if __name__ == "__main__":
    main()