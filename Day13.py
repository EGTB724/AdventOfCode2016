def main():
    inputNumber = 1352
    startCoord = (1,1)
    endCoord = (31,39)

    #First we need to generate the search space
    w, h = 50, 50
    grid = [["" for x in range(w)] for y in range(h)]

    for y, row in enumerate(grid):
        for x, col in enumerate(grid[y]):
            pt1 = x*x + 3*x + 2*x*y + y + y*y
            pt1 += inputNumber

            oneCounter = 0
            while pt1 != 0:
                if pt1%2 == 1:
                    oneCounter += 1
                pt1 //= 2

            if oneCounter%2 == 0:
                grid[y][x] = "."
            else:
                grid[y][x] = "#"


    #Do a bfs from start to finish
    open = [(startCoord[0], startCoord[1], 0)]
    visited = [(startCoord[0], startCoord[1])]


    while open:
        #Pop the next item to be visited
        currPair = open.pop(0)

        #Check if we're done
        if currPair[0] == endCoord[0] and currPair[1] == endCoord[1]:
            print(f"Part 1: {currPair[2]} ")
            break

        #Find the row and col
        currX = currPair[0]
        currY = currPair[1]
        currDistance = currPair[2]

        #Find possible moves from here
        # Add those indicies to OPEN if they are not already in visited
        if currX != 0:
            if grid[currY][currX-1] != "#":
                leftCoord = (currX-1, currY)
                if leftCoord not in visited:
                    open.append((leftCoord[0], leftCoord[1], currDistance + 1))
                    visited.append((leftCoord[0], leftCoord[1]))
        if currX != h-1:
            if grid[currY][currX + 1] != "#":
                rightCoord = (currX+1, currY)
                if rightCoord not in visited:
                    open.append((rightCoord[0], rightCoord[1], currDistance + 1))
                    visited.append((rightCoord[0], rightCoord[1]))
        if currY != 0:
            if grid[currY-1][currX] != "#":
                upCoord = (currX, currY-1)
                if upCoord not in visited:
                    open.append((upCoord[0], upCoord[1], currDistance + 1))
                    visited.append((upCoord[0], upCoord[1]))
        if currY != w-1:
            if grid[currY+1][currX] != "#":
                downCoord = (currX,currY+1)
                if downCoord not in visited:
                    open.append((downCoord[0], downCoord[1], currDistance + 1))
                    visited.append((downCoord[0], downCoord[1]))


    #Part 2

    open = [(startCoord[0], startCoord[1], 0)]
    visited = [(startCoord[0], startCoord[1])]

    while open:
        # Pop the next item to be visited
        currPair = open.pop(0)

        # Find the row and col
        currX = currPair[0]
        currY = currPair[1]
        currDistance = currPair[2]

        # Find possible moves from here
        # Add those indicies to OPEN if they are not already in visited
        if currX != 0:
            if grid[currY][currX - 1] != "#":
                leftCoord = (currX - 1, currY)
                if leftCoord not in visited:
                    if currDistance < 50:
                        open.append((leftCoord[0], leftCoord[1], currDistance + 1))
                        visited.append((leftCoord[0], leftCoord[1]))
        if currX != h - 1:
            if grid[currY][currX + 1] != "#":
                rightCoord = (currX + 1, currY)
                if rightCoord not in visited:
                    if currDistance < 50:
                        open.append((rightCoord[0], rightCoord[1], currDistance + 1))
                        visited.append((rightCoord[0], rightCoord[1]))
        if currY != 0:
            if grid[currY - 1][currX] != "#":
                upCoord = (currX, currY - 1)
                if upCoord not in visited:
                    if currDistance < 50:
                        open.append((upCoord[0], upCoord[1], currDistance + 1))
                        visited.append((upCoord[0], upCoord[1]))
        if currY != w - 1:
            if grid[currY + 1][currX] != "#":
                downCoord = (currX, currY + 1)
                if downCoord not in visited:
                    if currDistance < 50:
                        open.append((downCoord[0], downCoord[1], currDistance + 1))
                        visited.append((downCoord[0], downCoord[1]))

    print(f"Part 2: {len(visited)}")












if __name__ == "__main__":
    main()