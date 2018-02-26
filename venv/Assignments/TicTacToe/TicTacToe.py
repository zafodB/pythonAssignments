'''
 * Created by filip on 26/02/2018
'''

def main():

    board = [["." for j in range(3)] for i in range(3)]

    board = [[".", ".", "X"],
             [".", ".", "."],
             [".", ".", "X"]]

    def print_board(to_print):
        print("___________")

        for i in to_print:
            print("|", end="")
            for j in i:
                print(" " + str(j) + " ", end="")
            print("|")

        print("¯¯¯¯¯¯¯¯¯¯¯")

    def user_turn():
        print_board()

        while True:
            user_input = input("\n Please press number 1 - 9 to place X\n")
            if len(user_input) == 1:
                if user_input == "1" and board[0][0] == ".":
                        board[0][0] = "X"
                        break
                if user_input == "2" and board[0][1] == ".":
                        board[0][1] = "X"
                        break
                if user_input == "3" and board[0][2] == ".":
                        board[0][2] = "X"
                        break
                if user_input == "4" and board[1][0] == ".":
                        board[1][0] = "X"
                        break
                if user_input == "5" and board[1][1] == ".":
                        board[1][1] = "X"
                        break
                if user_input == "6" and board[1][2] == ".":
                        board[1][2] = "X"
                        break
                if user_input == "7" and board[2][0] == ".":
                        board[2][0] = "X"
                        break
                if user_input == "8" and board[2][1] == ".":
                        board[2][1] = "X"
                        break
                if user_input == "9" and board[2][2] == ".":
                        board[2][2] = "X"
                        break
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


    def ai_turn1():

        def find_best_move(on_map):
            pos_nxt_map = consider_posibilities(on_map, "O")

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

            return [best_v_x, best_v_y]

        nonlocal board

        best_vals1 = find_best_move(board)

        hypot_board = list(board)
        hypot_board[best_vals1[1]][best_vals1[0]] = "O"

        print_board(hypot_board)

        hypot_board2 = user_turn_by_ai(hypot_board)

        print_board(hypot_board2)

        # print("I think the best position for the tile would be: x=" + str(best_vals1[0]) + " y=" + str(best_vals1[1]))

        # user_turn_by_ai(hypot_board)

        def place_tile(x, y, char):
            nonlocal board
            board[y][x] = char

    def evaluate_turn(hboard, mx, my, mchar):
        if not is_valid_move(hboard, mx, my):
            return False
        if is_win_move(hboard, mx, my, mchar):
            return True
        if need_to_block(hboard, mx, my, mchar):
            return 50

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
                elif eval_res == 2:
                    next_turn_map[y][x] = 2

                elif eval_res:
                    next_turn_map[y][x] = 100

                x += 1
            y += 1
        # print_board(next_turn_map)

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
    ai_turn1()


main()
