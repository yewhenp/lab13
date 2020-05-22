"""
Module for tic-tac-toe game
"""

from board import Board


def main():
    """
    Main func
    """
    board = Board()
    print("Welcome to noliki game!")
    print("Here, computer will defeat you")

    print("\n", board, "\n")

    print("You should play, entering 2 numbers, "
          "like: 1 2. They should be between 0 and 2. "
          "First num - row, second - col")

    print("\nLet`s start!!!")

    while board.check_situation()[0] == 1:
        try:
            row, col = input("Please, enter 2 nums: ").split()
        except ValueError:
            print("Invalid coords")
            continue

        try:
            row = int(row)
            col = int(col)
        except ValueError:
            print("Entered not int nums")
            continue

        flag = board.make_move('x', row, col)
        if flag and board.check_situation()[0] == 1:
            print("\n", board, "\n")
            print("Computer moves")

            board.make_computer_move()
            print("\n", board, "\n")

    if board.check_situation()[1] == 'x':
        print("You won!!!")
    elif board.check_situation()[1] == 'o':
        print("Computer won")
    else:
        print("Equal")


if __name__ == '__main__':
    main()
