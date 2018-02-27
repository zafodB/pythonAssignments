'''
 * Created by filip on 26/02/2018
'''

import copy

def main():

    board = [["." for j in range(3)] for i in range(3)]

    board = [[".", ".", "."],
             [".", ".", "."],
             [".", ".", "."]]

    # y = 0
    # while y < 3:
    #     x = 0
    #     while x < 3:
    #         x += 1
    #     y += 1

    def print_board(to_print):
        print("___________")

        for i in to_print:
            print("|", end="")
            for j in i:
                print(" " + str(j) + " ", end="")
            print("|")

        print("¯¯¯¯¯¯¯¯¯¯¯")

    def user_turn():
        print_board(board)

        while True:
            user_input = input("\n Please press number 1 - 9 to place X\n")
            if len(user_input) == 1:
                if user_input == "1" and board[2][0] == ".":
                    return place_tile(0, 2, "X")
                if user_input == "2" and board[2][1] == ".":
                    return place_tile(1, 2, "X")
                if user_input == "3" and board[2][2] == ".":
                    return place_tile(2, 2, "X")
                if user_input == "4" and board[1][0] == ".":
                    return place_tile(0, 1, "X")
                if user_input == "5" and board[1][1] == ".":
                    return place_tile(1, 1, "X")
                if user_input == "6" and board[1][2] == ".":
                    return place_tile(2, 1, "X")
                if user_input == "7" and board[0][0] == ".":
                    return place_tile(0, 0, "X")
                if user_input == "8" and board[0][1] == ".":
                    return place_tile(1, 0, "X")
                if user_input == "9" and board[0][2] == ".":
                    return place_tile(2, 0, "X")
                print("Try again.")

    def user_turn_by_ai(hboard):

        possible_next_turn_map = consider_posibilities(hboard, "X")

        best_value = 0
        best_v_x = -1
        best_v_y = -1
        y = 0
        while y < 3:
            x = 0
            while x < 3:
                if possible_next_turn_map[y][x] > best_value:
                    best_value = possible_next_turn_map[y][x]
                    best_v_x = x
                    best_v_y = y
                x += 1

            y += 1

        hboard[best_v_y][best_v_x] = "X"

        return hboard

    def place_tile(x, y, char):
        nonlocal board
        board[y][x] = char

        return is_win_move(board, x, y, char)

    def ai_turn1():

        def find_best_move(on_map, char):
            pos_nxt_map = consider_posibilities(on_map, char)

            # print(pos_nxt_map)

            best_value = 0
            best_v_x = -1
            best_v_y = -1
            y = 0
            while y < 3:
                x = 0
                while x < 3:
                    if pos_nxt_map[y][x] > best_value:
                        best_value = pos_nxt_map[y][x]
                        best_v_x = x
                        best_v_y = y
                    x += 1

                y += 1

            return [best_v_x, best_v_y, best_value]

        nonlocal board

        next_turn_win = consider_posibilities(board, "O")
        need_break = False
        y = 0
        while y < 3:
            x = 0
            while x < 3:
                if next_turn_win[y][x] == 45 or next_turn_win[y][x] == 100:
                    need_break = True
                    break
                x += 1

            if need_break:
                break
            y += 1

        if need_break:
            if place_tile(x, y, "O"):
                return True

            # print_board(board)
        else:
            options = [[0 for l in range(3)] for k in range(3)]

            y = 0
            while y < 3:
                x = 0
                while x < 3:
                    # hypot_board = list(board)
                    # hypot_board = copy.copy(board)
                    hypot_board = [0 for l in range(3)]

                    i = 0
                    for row in board:
                        hypot_board[i] = list(row)
                        i += 1

                    # hypot_board = board[:]

                    hypot_board[y][x] = "O"
                    next_user_move = find_best_move(hypot_board, "X")
                    hypot_board[next_user_move[1]][next_user_move[0]] = "X"

                    options[y][x] = find_best_move(hypot_board, "O")

                    x += 1
                y += 1

            best_option_cost = 0
            best_option_x = 0
            best_option_y = 0

            for row in options:
                for cell in row:
                    if cell[2] > best_option_cost:
                        best_option_cost = cell[2]
                        best_option_x = cell[0]
                        best_option_y = cell[1]

            if place_tile(best_option_x, best_option_y, "O"):
                return True

        return False

    def evaluate_turn(hboard, mx, my, mchar):
        if not is_valid_move(hboard, mx, my):
            return False
        if is_win_move(hboard, mx, my, mchar):
            return True
        if need_to_block(hboard, mx, my, mchar):
            return 45

        return 2

    def consider_posibilities(hboard, nchar):
        next_turn_map = [[0 for j in range(3)] for i in range(3)]

        y = 0
        while y < 3:
            x = 0

            while x < 3:
                eval_res = evaluate_turn(hboard, x, y, nchar)
                if not eval_res:
                    x += 1
                    continue
                elif eval_res == 45:
                    next_turn_map[y][x] = 45
                elif eval_res == 2:
                    next_turn_map[y][x] = 2
                elif eval_res:
                    next_turn_map[y][x] = 100

                x += 1
            y += 1

        # print_board(next_turn_map)
        # print(next_turn_map)

        return next_turn_map

    def is_valid_move(hboard, x, y):
        return hboard[y][x] == "."

    def is_win_move(hboard, x, y, mchar):
        board_vals = [[0 for k in range(3)] for l in range(3)]

        # Turn board into values
        yi = 0
        while yi < 3:
            xi = 0
            while xi < 3:
                if hboard[yi][xi] == mchar:
                    board_vals[yi][xi] = 1
                xi += 1
            yi += 1

        board_vals[y][x] = 1

        # Check rows
        yi = 0
        while yi < 3:
            sum_win = 0
            xi = 0
            while xi < 3:
                sum_win += board_vals[yi][xi]
                xi += 1
            if sum_win == 3:
                return True
            yi += 1

        # Check columns
        yi = 0
        while yi < 3:
            sum_win = 0
            xi = 0
            while xi < 3:
                sum_win += board_vals[xi][yi]
                xi += 1
            if sum_win == 3:
                return True
            yi += 1

        # Check diagonals
        if board_vals[0][0] == 1 and board_vals[1][1] == 1 and board_vals[2][2] == 1:
            return True

        # Check diagonals
        if board_vals[0][2] == 1 and board_vals[1][1] == 1 and board_vals[2][0] == 1:
            return True

        return False

    def need_to_block(hboard, x, y, mchar):
        if mchar == "X":
            return is_win_move(hboard, x, y, "O")
        else:
            return is_win_move(hboard, x, y, "X")


    # def is_lose_move(x, y):
    #     print("a")

    # user_turn()
    # print_board()

    # print(is_win_move(board, 2, 1, "X"))

    # print(need_to_block(board, 0, 2, "0"))

    # print_board(board)

    tile = 0
    if input("Wanna start? y/n") == "y":

        user_turn()
        tile += 1

    game_over = False
    while not game_over and not tile == 9:

        tile += 1
        game_over = ai_turn1()

        if not game_over:

            tile += 1
            if user_turn():
                game_over = True

    print_board(board)
    print("Game finished.")

main()
