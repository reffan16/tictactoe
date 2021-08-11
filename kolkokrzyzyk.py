def restart():
    answer = input('Do you want to play again?\nType "yes" or "no".\n')
    if answer == 'yes':
        tictactoe()
    elif answer == 'no':
        exit()
    else:
        print('Answer not recognized.\n')
        restart()


def tictactoe():
    while True:
        cells = '         '
        who_moves = 1
        cells_list = [x for x in cells]

        def grid():
            if who_moves % 2 == 1:
                player = 'X'
            else:
                player = 'O'
            print(f'\nNow player {player} moves.')
            print("---------")
            print('| ' + cells_list[0] + ' ' + cells_list[1] + ' ' + cells_list[2] + ' |')
            print('| ' + cells_list[3] + ' ' + cells_list[4] + ' ' + cells_list[5] + ' |')
            print('| ' + cells_list[6] + ' ' + cells_list[7] + ' ' + cells_list[8] + ' |')
            print("---------")

        def check():
            row1 = cells_list[0:3]
            row2 = cells_list[3:6]
            row3 = cells_list[6:9]
            column1 = [cells_list[0], cells_list[3], cells_list[6]]
            column2 = [cells_list[1], cells_list[4], cells_list[7]]
            column3 = [cells_list[2], cells_list[5], cells_list[8]]
            diagonal1 = [cells_list[0], cells_list[4], cells_list[8]]
            diagonal2 = [cells_list[2], cells_list[4], cells_list[6]]
            win_con_x = ['X', 'X', 'X']
            win_con_o = ['O', 'O', 'O']
            matrix = [row1, row2, row3, column1, column2, column3, diagonal1, diagonal2]
            if win_con_x in matrix:
                print('Player X wins!\n')
                restart()
            elif win_con_o in matrix:
                print('Player O wins!\n')
                restart()
            elif (win_con_x not in matrix and win_con_o not in matrix) and ' ' not in cells_list:
                print("It's a draw!\n")
                restart()

        grid()

        while True:
            try:
                row_coord, column_coord = input('Enter the coordinates [x, y]: ').split()
            except ValueError:
                print('You must enter two numerical coordinates!')
                grid()
                continue
            if not row_coord.isnumeric():
                print('You should enter numbers!')
                grid()
            elif not column_coord.isnumeric():
                print('You should enter numbers!')
                grid()
            elif int(row_coord) not in range(1, 4) or int(column_coord) not in range(1, 4):
                print('Coordinates should be in range from 1 to 3!')
                grid()
            elif int(column_coord) in range(1, 4) and int(row_coord) in range(1, 4):
                index = ((int(row_coord) - 1) * 3) + (int(column_coord) + 2) - 3
                if cells_list[int(index)] == 'X' or cells_list[(int(index))] == 'O':
                    print('This cell is occupied! Choose another one!\n')
                    grid()
                elif who_moves % 2 == 1:
                    cells_list[int(index)] = 'X'
                    who_moves += 1
                    grid()
                    check()
                elif who_moves % 2 == 0:
                    cells_list[int(index)] = 'O'
                    who_moves += 1
                    grid()
                    check()


tictactoe()