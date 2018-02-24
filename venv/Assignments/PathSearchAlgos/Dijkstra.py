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
    # i = 1
    # while i < 10:
    #     if i not in to_visit:
    #         to_visit[i] = queue.Queue()
    #     to_visit[i].put([1, i])
    #     i += 1

    distance_map = [[0 for i in range(map_dim_x)] for j in range(map_dim_y)]
    visited_map = [[0 for i in range(map_dim_x)] for j in range(map_dim_y)]

    # visit_stack =
    # print(visited_map)

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

        if not visited_map[y][x] == 1:
            visited_map[y][x] = 1

            if not x - 1 < 0 and not visited_map[y][x - 1] == 1:
                distance = distance_map[y][x] + world_map[y][x - 1]

                if distance_map[y][x - 1] == 0:
                    distance_map[y][x - 1] = distance
                elif distance < distance_map[y][x - 1]:
                    distance_map[y][x - 1] = distance

                add_to_visitlist(distance, x - 1, y)

            if not y - 1 < 0 and not visited_map[y - 1][x] == 1:
                distance = distance_map[y][x] + world_map[y - 1][x]

                if distance_map[y - 1][x] == 0:
                    distance_map[y - 1][x] = distance
                elif distance < distance_map[y - 1][x]:
                    distance_map[y - 1][x] = distance

                add_to_visitlist(distance, x, y - 1)

            if not x + 1 >= map_dim_x and not visited_map[y][x + 1] == 1:
                distance = distance_map[y][x] + world_map[y][x + 1]

                if distance_map[y][x + 1] == 0:
                    distance_map[y][x + 1] = distance
                elif distance < distance_map[y][x + 1]:
                    distance_map[y][x + 1] = distance

                add_to_visitlist(distance, x + 1, y)

            if not y + 1 >= map_dim_y and not visited_map[y + 1][x] == 1:
                distance = distance_map[y][x] + world_map[y + 1][x]

                if distance_map[y + 1][x] == 0:
                    distance_map[y + 1][x] = distance
                elif distance < distance_map[y + 1][x]:
                    distance_map[y + 1][x] = distance

                add_to_visitlist(distance, x, y + 1)

    def set_start(x,y):
        nonlocal world_map
        world_map[y][x] = -1

    def set_goal(x,y):
        nonlocal world_map
        world_map[y][x] = -1

    def print_visited(pmap):
        nonlocal map_dim_y
        nonlocal map_dim_x

        y = 0
        while y < (map_dim_y):
            x = 0
            if y == 0:

                brd = 0
                while brd < (map_dim_x):
                    print("____", end="")
                    brd += 1
                print("__")
            print("|", end="")

            while x < (map_dim_x):
                if (pmap[y][x] == -1):
                    print("    ", end="")
                else:
                    print("%03d " % (pmap[y][x]), end="")
                x += 1
            print("|")
            y += 1

        brd = 0
        while brd < map_dim_x:
            print("¯¯¯¯", end="")
            brd += 1
        print("¯¯")

    set_start(start_x, start_y)
    set_goal(goal_x, goal_y)
    print_visited(world_map)

    dijkstra(start_x, start_y)

    while to_visit.keys():
        i = 0
        while i < 200:
            if i in to_visit:
                if to_visit[i].empty():
                    del to_visit[i]
                else:
                    xypair = to_visit[i].get()
                    dijkstra(xypair[0], xypair[1])
            i += 1


    print_visited(visited_map)
    print_visited(distance_map)

main()
