'''
 * Created by filip on 26/02/2018
'''

import copy


def main():
    board = [["." for j in range(3)] for i in range(3)]

    difficulty = 3

    # Prints out any board
    def print_board(to_print):
        print("___________")

        for i in to_print:
            print("|", end="")
            for j in i:
                print(" " + str(j) + " ", end="")
            print("|")

        print("¯¯¯¯¯¯¯¯¯¯¯")

    # Takes user's input and calls place_tile(), if move is possible. Returns True, if it's a winning move, False otherwise.
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

    # Places tile on board and returns True, if it's a winning move.
    def place_tile(x, y, char):
        nonlocal board
        board[y][x] = char

        return is_win_move(board, x, y, char)

    # Takes board, coordinates and character as arguments. Places character onto the board on specified coordinates and returns, if this is a winning move.
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

    # Makes AI move, depending on the selected level of difficulty.
    def ai_turn():

        # Creates a copy of a board (to test out hypothetical moves).
        def copy_board(in_board):
            out_board = [0 for l in range(3)]
            i = 0
            for row in in_board:
                out_board[i] = list(row)
                i += 1
            return out_board

        # Looks at passed board and considers immediate wins or losses.
        def consider_possibilities(hboard, nchar):
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
                    elif eval_res == 100:
                        next_turn_map[y][x] = 100

                    x += 1
                y += 1

            return next_turn_map

        # Checks, if placing a tile on specified coordinate results in win or a lose.
        def evaluate_turn(hboard, mx, my, mchar):
            if not is_valid_move(hboard, mx, my):
                return False
            if is_win_move(hboard, mx, my, mchar):
                return 100
            if need_to_block(hboard, mx, my, mchar):
                return 45

            return 2

        # Checks, if a move is possible (that there are no tiles in the way)
        def is_valid_move(hboard, x, y):
            return hboard[y][x] == "."

        # Checks if next move can be a winning move for the opposing player.
        def need_to_block(hboard, x, y, mchar):
            if mchar == "X":
                return is_win_move(hboard, x, y, "O")
            else:
                return is_win_move(hboard, x, y, "X")

        # Checks, if it can immediately win or lose. If yes, returns coordinates where to place tile appropriately.
        def next_turn_win_lose(hboard, mchar):
            next_turn_win = consider_possibilities(hboard, mchar)
            found_next_turn = False
            possible_moves = 0
            next_move_x = -1
            next_move_y = -1

            y = 0
            while y < 3:
                x = 0
                while x < 3:

                    # Can it win in next turn?
                    if next_turn_win[y][x] == 100:
                        found_next_turn = True
                        next_move_x = x
                        next_move_y = y
                        return [found_next_turn, next_move_x, next_move_y, -1]

                    # Does it need to block in next turn?
                    elif next_turn_win[y][x] == 45:
                        next_move_x = x
                        next_move_y = y
                        found_next_turn = True

                    elif not next_turn_win[y][x] == 0:

                        # Is there only one available move?
                        possible_moves += 1
                        if possible_moves == 1 and not found_next_turn:
                            next_move_x = x
                            next_move_y = y
                    x += 1

                y += 1

            return [found_next_turn, next_move_x, next_move_y, possible_moves]

        nonlocal board

        # Difficulty level 1
        # Checks if AI can win or lose immediately. If it can win, it wins. If it could lose, it blocks.
        # Also checks if this is the last turn. If so, places the  last tile (and no further calculations are performed).
        immediate_turn = next_turn_win_lose(board, "O")

        if immediate_turn[0]:
            return place_tile(immediate_turn[1], immediate_turn[2], "O")
        elif immediate_turn[3] == 1:
            return place_tile(immediate_turn[1], immediate_turn[2], "O")

        # Difficulty level 1
        else:
            options = [[0 for l in range(3)] for k in range(3)]

            # Consider placing own tile on every available position on the board.
            y = 0
            while y < 3:
                x = 0
                while x < 3:

                    if is_valid_move(board, x, y):
                        # Copying exiting game board to a hypothetical one.
                        hypot_board = copy_board(board)

                        # Place a tile onto the hypothetical board
                        hypot_board[y][x] = "O"

                        # After own tile has been placed on the hypothetical board, consider every possible next user move.
                        y1 = 0
                        while y1 < 3:
                            x1 = 0
                            while x1 < 3:

                                if is_valid_move(hypot_board, x1, y1):
                                    hypot_board2 = copy_board(hypot_board)
                                    hypot_board2[y1][x1] = "X"

                                    # Difficulty level 2
                                    if not next_turn_win_lose(hypot_board2, "O")[3] == -1 and not difficulty == 1:

                                        block_rate = 0
                                        y2 = 0
                                        while y2 < 3:
                                            x2 = 0
                                            while x2 < 3:
                                                if is_valid_move(hypot_board2, x2, y2) and not is_win_move(hypot_board2,
                                                                                                           x2, y2, "O"):
                                                    if need_to_block(hypot_board2, x2, y2, "O"):
                                                        block_rate += 1

                                                    hypot_board3 = copy_board(hypot_board2)
                                                    hypot_board3[y2][x2] = "O"

                                                    # Difficulty level 3
                                                    if not next_turn_win_lose(hypot_board3, "X")[
                                                               3] == -1 and difficulty == 3:
                                                        y3 = 0
                                                        while y3 < 3:
                                                            x3 = 0
                                                            while x3 < 3:
                                                                if is_valid_move(hypot_board3, x3,
                                                                                 y3) and not is_win_move(hypot_board3,
                                                                                                         x3, y3, "X"):
                                                                    hypot_board4 = copy_board(hypot_board3)
                                                                    hypot_board4[y3][x3] = "X"

                                                                    block_rate2 = 0

                                                                    for row in consider_possibilities(hypot_board4,
                                                                                                      "O"):
                                                                        for item in row:
                                                                            if item == 45:
                                                                                block_rate2 += 1

                                                                    if block_rate2 > 1:
                                                                        options[y][x] -= 10

                                                                x3 += 1
                                                            y3 += 1
                                                x2 += 1
                                            y2 += 1

                                        if block_rate > 1:
                                            options[y][x] -= 20

                                x1 += 1
                            y1 += 1
                    else:
                        options[y][x] = -550

                    x += 1
                y += 1

            best_option_cost = -2000
            best_option_x = 0
            best_option_y = 0

            # Find the best move based on calculated weight of options.
            y = 0
            while y < 3:
                x = 0
                while x < 3:

                    if options[y][x] > best_option_cost:
                        best_option_cost = options[y][x]
                        best_option_x = x
                        best_option_y = y

                    x += 1
                y += 1

            # Place the tile and return True if it is a winning move.
            return place_tile(best_option_x, best_option_y, "O")

    # Starts the game
    def play_game():
        tile = 0
        nonlocal difficulty

        user_input = input("Select the level of difficulty: (1 - 3)")

        if user_input == "1":
            difficulty = 1
        elif user_input == "2":
            difficulty = 2

        if input("Wanna start? y/n") == "y":
            user_turn()
            tile += 1

        game_over = False
        while not game_over and not tile == 9:
            tile += 1
            game_over = ai_turn()

            if not game_over and not tile == 9:
                tile += 1
                game_over = user_turn()

        print_board(board)
        print("Game finished.")

    play_game()


main()
