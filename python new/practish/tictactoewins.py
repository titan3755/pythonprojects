def who_won(board):
    list_1 = board[0]
    list_2 = board[1]
    list_3 = board[2]
    count_x = 0
    count_O = 0
    main_list = []
    for x in list_1:
        main_list.append(x)
    for y in list_2:
        main_list.append(y)
    for z in list_3:
        main_list.append(z)
    for item in main_list:
        if item == 'X':
            count_x += 1
        elif item == 'O':
            count_O += 1
    if count_x % 2 == 0:
        return 'O'
    else:
        return 'X'


print(who_won([
    ["O", "X", "X"],
    ["O", "O", "X"],
    ["O", "X", "O"],
]))
