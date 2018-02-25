'''
 * Created by filip on 22/02/2018
'''

import queue


def main():
    world_map = [[3, 8, 2, 8, 10, 5, 5, 9, 5, 4, 4, 4, 5, 10, 4],
                 [1, 6, 8, 1, 4, 1, 3, 5, 4, 1, 7, 8, 1, 7, 9],
                 [4, 7, 7, 2, 10, 1, 1, 1, 2, 1, 5, 1, 9, 7, 9],
                 [5, 7, 2, 5, 2, 2, 9, 3, 7, 3, 1, 4, 3, 10, 4],
                 [9, 5, 1, 1, 2, 9, 9, 6, 3, 3, 3, 5, 4, 9, 3],
                 [7, 8, 1, 10, 5, 9, 1, 3, 10, 4, 7, 2, 10, 5, 8],
                 [7, 8, 7, 8, 9, 9, 2, 5, 9, 8, 4, 8, 1, 3, 4],
                 [5, 3, 7, 10, 6, 5, 4, 7, 4, 7, 9, 8, 10, 9, 4],
                 [9, 4, 8, 7, 5, 9, 9, 2, 1, 2, 6, 7, 5, 4, 4],
                 [1, 10, 1, 8, 10, 10, 7, 3, 4, 8, 7, 5, 9, 6, 2],
                 [2, 2, 9, 4, 3, 10, 7, 7, 10, 10, 4, 6, 4, 7, 2],
                 [10, 10, 1, 6, 5, 7, 5, 7, 1, 3, 8, 7, 9, 7, 8],
                 [7, 4, 6, 9, 2, 4, 6, 5, 7, 9, 8, 9, 9, 9, 9],
                 [9, 5, 8, 6, 3, 8, 2, 2, 4, 3, 10, 9, 1, 3, 5],
                 [6, 10, 8, 6, 2, 2, 9, 1, 1, 1, 8, 9, 1, 6, 2],
                 [5, 1, 4, 7, 8, 10, 3, 7, 2, 1, 1, 1, 1, 10, 2],
                 [3, 1, 6, 4, 4, 10, 10, 6, 7, 4, 3, 4, 1, 5, 4],
                 [6, 4, 8, 9, 4, 4, 5, 4, 6, 5, 8, 7, 2, 9, 5]]

    map_dim_y = len(world_map)
    map_dim_x = len(world_map[0])

    start_x = 4
    start_y = 4

    goal_x = 12
    goal_y = 13

    to_visit = dict()

    distance_map = [[[0 for k in range(2)] for i in range(map_dim_x)] for j in range(map_dim_y)]
    visited_map = [[0 for i in range(map_dim_x)] for j in range(map_dim_y)]

    def dijkstra(x, y):

        def add_to_visitlist(dist, vx, vy):
            nonlocal to_visit

            if distance not in to_visit:
                to_visit[dist] = queue.Queue()
            to_visit[dist].put([vx, vy])

        nonlocal to_visit
        nonlocal visited_map
        nonlocal map_dim_x
        nonlocal map_dim_y
        nonlocal goal_x
        nonlocal goal_y

        print_visited([[row[0] for row in distance_map[i]] for i in range(map_dim_y)])

        if not visited_map[y][x] == 1:
            visited_map[y][x] = 1

            # 1 - right
            # 2 - bottom
            # 3 - left
            # 4 - top

            # Came from the right
            if not x - 1 < 0 and not visited_map[y][x - 1] == 1:
                distance = distance_map[y][x][0] + world_map[y][x - 1]

                if distance_map[y][x - 1][0] == 0:
                    distance_map[y][x - 1][0] = distance
                    distance_map[y][x - 1][1] = 1
                    if x - 1 == goal_x and y == goal_y:
                        return True
                    else:
                        add_to_visitlist(distance, x - 1, y)

            # Came from the bottom
            if not y - 1 < 0 and not visited_map[y - 1][x] == 1:
                distance = distance_map[y][x][0] + world_map[y - 1][x]

                if distance_map[y - 1][x][0] == 0:
                    distance_map[y - 1][x][0] = distance
                    distance_map[y - 1][x][1] = 2
                    if x == goal_x and y - 1 == goal_y:
                        return True
                    else:
                        add_to_visitlist(distance, x, y - 1)

            # Came from the left
            if not x + 1 >= map_dim_x and not visited_map[y][x + 1] == 1:
                distance = distance_map[y][x][0] + world_map[y][x + 1]

                if distance_map[y][x + 1][0] == 0:
                    distance_map[y][x + 1][0] = distance
                    distance_map[y][x + 1][1] = 3
                    if x + 1 == goal_x and y == goal_y:
                        return True
                    else:
                        add_to_visitlist(distance, x + 1, y)

            # Came from the top
            if not y + 1 >= map_dim_y and not visited_map[y + 1][x] == 1:
                distance = distance_map[y][x][0] + world_map[y + 1][x]

                if distance_map[y + 1][x][0] == 0:
                    distance_map[y + 1][x][0] = distance
                    distance_map[y + 1][x][1] = 4
                    if x == goal_x and y + 1 == goal_y:
                        return True
                    else:
                        add_to_visitlist(distance, x, y + 1)

    def print_visited(pmap):
        nonlocal map_dim_y
        nonlocal map_dim_x

        y = 0
        while y < (map_dim_y):
            x = 0
            if y == 0:

                brd = 0
                while brd < (map_dim_x):
                    print("___", end="")
                    brd += 1
                print("__")
            print("|", end="")

            while x < (map_dim_x):
                if (pmap[y][x] == -1):
                    print("   ", end="")
                elif (pmap[y][x] == 0):
                    print("   ", end="")
                else:
                    print("%02d " % (pmap[y][x]), end="")
                x += 1
            print("|")
            y += 1

        brd = 0
        while brd < map_dim_x:
            print("¯¯¯", end="")
            brd += 1
        print("¯¯")

    def print_path(pmap):
        nonlocal map_dim_y
        nonlocal map_dim_x
        nonlocal distance_map

        y = 0
        while y < (map_dim_y):
            x = 0
            if y == 0:

                brd = 0
                while brd < (map_dim_x):
                    print("___", end="")
                    brd += 1
                print("__")
            print("|", end="")

            while x < (map_dim_x):
                if (pmap[y][x] == 1):
                    print("%02d " % (distance_map[y][x][0]), end="")
                elif (pmap[y][x] == 0):
                    print("   ", end="")

                x += 1
            print("|")
            y += 1

        brd = 0
        while brd < map_dim_x:
            print("¯¯¯", end="")
            brd += 1
        print("¯¯")

    def make_path(pmap):
        nonlocal visited_map
        nonlocal goal_x
        nonlocal goal_y
        nonlocal start_x
        nonlocal start_y

        visited_map = [[0 for i in range(map_dim_x)] for j in range(map_dim_y)]

        def create_path(x, y):
            nonlocal start_x
            nonlocal start_y

            visited_map[y][x] = 1

            if pmap[y][x][1] == 1:
               create_path(x + 1, y)
            elif pmap[y][x][1] == 2:
                create_path(x, y + 1)
            elif pmap[y][x][1] == 3:
                create_path(x - 1, y)
            elif pmap[y][x][1] == 4:
                create_path(x, y - 1)

        create_path(goal_x, goal_y)

    print_visited(world_map)

    dijkstra(start_x, start_y)

    goal_found = False
    while to_visit.keys():
        if goal_found:
            break
        i = 0
        while i < 100:
            if goal_found:
                break

            if i in to_visit:
                while not to_visit[i].empty():
                    xypair = to_visit[i].get()
                    if dijkstra(xypair[0], xypair[1]):
                        goal_found = True
                        break

                del to_visit[i]
            i += 1

    # distance_map2 = [[row[0] for row in distance_map[i]] for i in range(map_dim_y)]
    print_visited([[row[0] for row in distance_map[i]] for i in range(map_dim_y)])

    make_path(distance_map)
    print_path(visited_map)


main()
