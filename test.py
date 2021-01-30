# some variables

board_var: list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player = "X"
run = True
main_run: bool = True


# printing the field
def field():
    print(f"{board_var[0]} | {board_var[1]} | {board_var[2]}")
    print("---------")
    print(f"{board_var[3]} | {board_var[4]} | {board_var[5]}")
    print("---------")
    print(f"{board_var[6]} | {board_var[7]} | {board_var[8]}")


# convert input
def eingabe():
    while True:
        x = input("Which position do you want to set on? ")
        if x == "1" and board_var[0] == " ":
            board_var[0] = player
            break
        elif x == "2" and board_var[1] == " ":
            board_var[1] = player
            break
        elif x == "3" and board_var[2] == " ":
            board_var[2] = player
            break
        elif x == "4" and board_var[3] == " ":
            board_var[3] = player
            break
        elif x == "5" and board_var[4] == " ":
            board_var[4] = player
            break
        elif x == "6" and board_var[5] == " ":
            board_var[5] = player
            break
        elif x == "7" and board_var[6] == " ":
            board_var[6] = player
            break
        elif x == "8" and board_var[7] == " ":
            board_var[7] = player
            break
        elif x == "9" and board_var[8] == " ":
            board_var[8] = player
            break
        else:
            print("1 | 2 | 3")
            print("---------")
            print("4 | 5 | 6")
            print("---------")
            print("7 | 8 | 9")


# is there a winner already
def winner():
    if board_var[0] == board_var[1] == board_var[2] == "X" or board_var[0] == board_var[1] == board_var[2] == "O":
        return False
    elif board_var[3] == board_var[4] == board_var[5] == "X" or board_var[3] == board_var[4] == board_var[5] == "O":
        return False
    elif board_var[6] == board_var[7] == board_var[8] == "X" or board_var[6] == board_var[7] == board_var[8] == "O":
        return False
    elif board_var[0] == board_var[3] == board_var[6] == "X" or board_var[0] == board_var[3] == board_var[6] == "O":
        return False
    elif board_var[1] == board_var[4] == board_var[7] == "X" or board_var[1] == board_var[4] == board_var[7] == "O":
        return False
    elif board_var[2] == board_var[5] == board_var[8] == "X" or board_var[2] == board_var[5] == board_var[8] == "O":
        return False
    elif board_var[0] == board_var[4] == board_var[8] == "X" or board_var[0] == board_var[4] == board_var[8] == "O":
        return False
    elif board_var[2] == board_var[4] == board_var[6] == "X" or board_var[2] == board_var[4] == board_var[6] == "O":
        return False
    else:
        return True


# test whether the board is full
def board_full():
    if board_var[0] != " " and board_var[1] != " " and board_var[2] != " " and board_var[3] != " " and board_var[
        4] != " " and board_var[5] != " " and \
            board_var[6] != " " and board_var[7] != " " and board_var[8] != " ":
        print("draw!")
        x = input("write \"play\" to restart: ")
        if x != "play":
            print("Bye")
            run = False
        else:

            field()


# main program


while main_run:
    field()
    while run:

        eingabe()
        if player == "X":
            player = "O"
        else:
            player = "X"
        field()
        run = winner()
        if run:
            board_full()

    if player == "X":
        player = "O"
    else:
        player = "X"

    board_var = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    print("Winner is player ", player)

    while True:
        again = input("Wanna play again?")
        if again == "no":
            print("Bye")
            main_run = False
            break
        elif again == "yes":
            print("Lets go for another round :)")
            run = True
            break
        else:
            print("yes = play again\nno  = dont play again")
