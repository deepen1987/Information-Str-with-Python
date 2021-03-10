# Tic Tac Toe
import sys

game_list = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
winner = False
count = 0


def game_generator1(num):
    if game_list[num - 1] == " ":
        game_list[num - 1] = "X"
        return True
    else:
        return False


def game_generator2(num2):
    if game_list[num2 - 1] == " ":
        game_list[num2 - 1] = "O"
        return True
    else:
        return False


def verify(args):
    if game_list[0] == game_list[1] == game_list[2] == args:
        # print(f"Winner is {player}")
        return True
    elif game_list[3] == game_list[4] == game_list[5] == args:
        # print(f"Winner is {player}")
        return True
    elif game_list[6] == game_list[7] == game_list[8] == args:
        # print(f"Winner is {player}")
        return True
    elif game_list[0] == game_list[3] == game_list[6] == args:
        # print(f"Winner is {player}")
        return True
    elif game_list[1] == game_list[4] == game_list[7] == args:
        # print(f"Winner is {player}")
        return True
    elif game_list[2] == game_list[5] == game_list[8] == args:
        # print(f"Winner is {player}")
        return True
    elif game_list[0] == game_list[4] == game_list[8] == args:
        # print(f"Winner is {player}")
        return True
    elif game_list[2] == game_list[4] == game_list[6] == args:
        # print(f"Winner is {player}")
        return True


def game_display():
    print(f"""{game_list[0]} |{game_list[1]} |{game_list[2]}
--+--+---""")
    print(f"""{game_list[3]} |{game_list[4]} |{game_list[5]}
--+--+---""")
    print(f"{game_list[6]} |{game_list[7]} |{game_list[8]}")


game_display()
while not winner and count <= 9:
    valid_input = False
    while not valid_input:
        try:
            player1 = int(input("Player 1 please select the position for X: "))
            valid_input = True
            while not game_generator1(player1):
                player1 = int(input("Player 1 please select the position for X: "))
                valid_input = True
        except ValueError:
            print("Please enter integer 1 - 9")
            valid_input = False
    valid_input = False
    game_display()
    winner = verify("X")
    if winner:
        print(f"Winner is Player 1")
        replay = input("Do you want to play again press Y else press anything to exit: ").upper()
        if replay == "Y":
            game_list = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
            winner = False
            count = 0
            game_display()
            continue
        if replay != "Y":
            print("Bye Bye!!!")
            sys.exit()
    count += 1
    if count == 9:
        print("Game Draw....")
        break
    while not valid_input:
        try:
            player2 = int(input("Player 2 please select the position for O: "))
            valid_input = True
            while not game_generator2(player2):
                player2 = int(input("Player 2 please select the position for O: "))
                valid_input = True
        except ValueError:
            valid_input = False
    game_display()
    winner = verify("O")
    if winner:
        print(f"Winner is Player 1")
        replay = input("Do you want to play again press Y else press anything to exit: ").upper()
        if replay == "Y":
            game_list = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]
            winner = False
            count = 0
            game_display()
            continue
        if replay != "Y":
            print("Bye Bye!!!")
            sys.exit()
    count += 1
