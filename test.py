list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player = "X"
run = True

def feld():
    print(f"{list[0]} | {list[1]} | {list[2]}")
    print("---------")
    print(f"{list[3]} | {list[4]} | {list[5]}")
    print("---------")
    print(f"{list[6]} | {list[7]} | {list[8]}")

def eingabe():
    while True:
        x = input("Auf welches Feld willst du setzen? ")
        if x == "1" and list[0] == " ":
            list[0] = player
            break
        elif x == "2" and list[1] == " ":
            list[1] = player
            break
        elif x == "3" and list[2] == " ":
            list[2] = player
            break
        elif x == "4" and list[3] == " ":
            list[3] = player
            break
        elif x == "5" and list[4] == " ":
            list[4] = player
            break
        elif x == "6" and list[5] == " ":
            list[5] = player
            break
        elif x == "7" and list[6] == " ":
            list[6] = player
            break
        elif x == "8" and list[7] == " ":
            list[7] = player
            break
        elif x == "9" and list[8] == " ":
            list[8] = player
            break
        else:
            print("1 | 2 | 3")
            print("---------")
            print("4 | 5 | 6")
            print("---------")
            print("7 | 8 | 9")

def winner():

    if list[0] == list[1] == list[2] == "X" or list[0] == list[1] == list[2] == "O":
        return False
    elif list[3] == list[4] == list[5] == "X" or list[3] == list[4] == list[5] == "O":
        return False
    elif list[6] == list[7] == list[8] == "X" or list[6] == list[7] == list[8] == "O":
        return False
    elif list[0] == list[3] == list[6] == "X" or list[0] == list[3] == list[6] == "O":
        return False
    elif list[1] == list[4] == list[7] == "X" or list[1] == list[4] == list[7] == "O":
        return False
    elif list[2] == list[5] == list[8] == "X" or list[2] == list[5] == list[8] == "O":
        return False
    elif list[0] == list[4] == list[8] == "X" or list[0] == list[4] == list[8] == "O":
        return False
    elif list[2] == list[4] == list[6] == "X" or list[2] == list[4] == list[6] == "O":
        return False
    else:
        return True


while run:
    feld()
    eingabe()
    if player == "X":
        player = "O"
    else:
        player = "X"
    run = winner()

if player == "X":
    player = "O"
else:
    player = "X"

print("Winner is player ", player)