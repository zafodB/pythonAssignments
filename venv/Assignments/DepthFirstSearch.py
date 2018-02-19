'''
 * Created by filip on 19/02/2018
'''

def main():

    xStart = 1
    yStart = 1

    count = 0

    xGoal = 10
    yGoal = 9

    goalFound = False

    myMap = [[-1, -2, -1, -2, -1, -2, -1, -1, -1, -2, -1, -1],
             [-1, -1, -1, -1, -1, -2, -1, -2, -1, -2, -2, -1],
             [-1, -2, -1, -2, -1, -2, -1, -2, -1, -1, -1, -1],
             [-1, -2, -1, -2, -1, -1, -1, -2, -1, -2, -2, -2],
             [-1, -2, -1, -2, -1, -2, -1, -1, -1, -2, -1, -1],
             [-1, -2, -1, -2, -1, -2, -2, -2, -1, -2, -1, -1],
             [-1, -2, -1, -2, -1, -1, -1, -2, -1, -1, -1, -1],
             [-1, -2, -1, -2, -2, -1, -1, -2, -1, -2, -2, -1],
             [-1, -1, -1, -1, -2, -1, -1, -1, -1, -2, -1, -1],
             [-2, -1, -2, -2, -2, -2, -1, -2, -1, -2, -1, -1],
             [-1, -1, -1, -1, -1, -2, -1, -2, -1, -2, -1, -1],
             [-1, -2, -1, -2, -1, -1, -1, -2, -1, -1, -1, -1]]

    def dsf(x, y):
        nonlocal myMap
        nonlocal goalFound
        nonlocal count

        count += 1
        mapLengthX = len(myMap[0])
        mapLengthY = len(myMap)

        # print("x: " + str(x) + " y: " + str(y))

        myMap[x][y] = 0
        print_map(myMap)

        if x == xGoal and y == yGoal:
            goalFound = True
            print("Goal Found at: " + str(x) + " and " + str(y) + " after " + str(count) + " steps.")

        if y + 1 < mapLengthY and not myMap[x][y + 1] == 0 and not myMap[x][y + 1] == -2 and not goalFound:
            dsf(x, y + 1)
        if x + 1 < mapLengthX and not myMap[x + 1][y] == 0 and not myMap[x + 1][y] == -2 and not goalFound:
            dsf(x + 1, y)
        if y - 1 >= 0 and not myMap[x][y - 1] == 0 and not myMap[x][y - 1] == -2 and not goalFound:
            dsf(x, y - 1)
        if x - 1 >= 0 and not myMap[x - 1][y] == 0 and not myMap[x - 1][y] == -2 and not goalFound:
            dsf(x - 1, y)

    def print_map(my_map):
        y = 0
        while y < len(my_map):
            x = 0
            if y == 0:
                brd = len(my_map[y])
                while brd > 0:
                    print("__", end="")
                    brd -= 1
                print("__")
            print("|", end="")

            while x < len(my_map[y]):
                if my_map[x][y] == -1:
                    print("  ", end="")
                elif (myMap[x][y]) == -3:
                    print("OO", end="")
                elif (myMap[x][y]) == 0:
                    print(". ", end="")
                else:
                    print("##", end="")
                x += 1
            print("|")
            y += 1

        brd = len(myMap[y-1])
        while brd > 0:
            print("¯¯", end="")
            brd -= 1
        print("¯¯")

    def setStart(xStartF, yStartF):
        nonlocal myMap
        myMap[xStartF][yStartF] = -3

    def setGoal(xGoalF, yGoalF):
        nonlocal myMap
        myMap[xGoalF][yGoalF] = -3

    setGoal(xGoal, yGoal)
    setStart(xStart, yStart)

    print_map(myMap)
    dsf(xStart, yStart)

    print_map(myMap)


main()
