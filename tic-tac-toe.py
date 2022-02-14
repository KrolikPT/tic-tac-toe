import tabulate 
import pandas as pd
import os

endgame = False
player_1 =  "\033[1;32mX\033[0m"
player_2 = "\033[1;31mO\033[0m"


def check_win(tabuleiro, turn, plays):

    check = False
    winner = ""

    # Check draw
    if plays == 9:
        check = True
        winner = "DRAW"

    if turn == "P1":
        # Win possibilities
            # 1 2 3
        if ((tabuleiro["row_1"][0] == player_1 and tabuleiro["row_2"][0] == player_1 and tabuleiro["row_3"][0] == player_1) or 
            # 4 5 6
            (tabuleiro["row_1"][1] == player_1 and tabuleiro["row_2"][1] == player_1 and tabuleiro["row_3"][1] == player_1) or
            # 7 8 9
            (tabuleiro["row_1"][1] == player_1 and tabuleiro["row_2"][1] == player_1 and tabuleiro["row_3"][1] == player_1) or 
            # 1 4 7
            (tabuleiro["row_1"][0] == player_1 and tabuleiro["row_1"][1] == player_1 and tabuleiro["row_1"][2] == player_1) or 
            # 2 5 8
            (tabuleiro["row_2"][0] == player_1 and tabuleiro["row_2"][1] == player_1 and tabuleiro["row_2"][2] == player_1) or 
            # 3 6 9
            (tabuleiro["row_3"][0] == player_1 and tabuleiro["row_3"][1] == player_1 and tabuleiro["row_3"][2] == player_1) or 
            # 1 5 9
            (tabuleiro["row_1"][0] == player_1 and tabuleiro["row_2"][1] == player_1 and tabuleiro["row_3"][2] == player_1) or 
            # 3 5 7
            (tabuleiro["row_3"][0] == player_1 and tabuleiro["row_2"][1] == player_1 and tabuleiro["row_1"][2] == player_1)):
            
            check = True
            winner = "P1"

    elif turn == "P2":
        # Win possibilities
            # 1 2 3
        if ((tabuleiro["row_1"][0] == player_2 and tabuleiro["row_2"][0] == player_2 and tabuleiro["row_3"][0] == player_2) or 
            # 4 5 6
            (tabuleiro["row_1"][1] == player_2 and tabuleiro["row_2"][1] == player_2 and tabuleiro["row_3"][1] == player_2) or
            # 7 8 9
            (tabuleiro["row_1"][1] == player_2 and tabuleiro["row_2"][1] == player_2 and tabuleiro["row_3"][1] == player_2) or 
            # 1 4 7
            (tabuleiro["row_1"][0] == player_2 and tabuleiro["row_1"][1] == player_2 and tabuleiro["row_1"][2] == player_2) or 
            # 2 5 8
            (tabuleiro["row_2"][0] == player_2 and tabuleiro["row_2"][1] == player_2 and tabuleiro["row_2"][2] == player_2) or 
            # 3 6 9
            (tabuleiro["row_3"][0] == player_2 and tabuleiro["row_3"][1] == player_2 and tabuleiro["row_3"][2] == player_2) or 
            # 1 5 9
            (tabuleiro["row_1"][0] == player_2 and tabuleiro["row_2"][1] == player_2 and tabuleiro["row_3"][2] == player_2) or 
            # 3 5 7
            (tabuleiro["row_3"][0] == player_2 and tabuleiro["row_2"][1] == player_2 and tabuleiro["row_1"][2] == player_2)):
            
            check = True
            winner = "P2"


    # Victory message
    if check and winner == "P1":    
        print(display_board(tabuleiro))
        print("\nPlayer 1 wins!!!")  
        input()
        exit()
    elif check and winner == "P2":
        print(display_board(tabuleiro))
        print("\nPlayer 2 wins!!!")
        input()
        exit()
    elif check and winner == "DRAW":
        print(display_board(tabuleiro))
        print("\nDRAW!!!")
        input()
        exit()


# Show boardgame
def display_board(tabuleiro):

    os.system("@cls||clear")
    
    print("*************************************************************")
    print("************************ TIC TAC TOE ************************")
    print("*************************************************************\n")

    tabuleiro_jogo = pd.DataFrame(tabuleiro)
    return tabulate.tabulate(tabuleiro_jogo, tablefmt="grid", showindex=False)


def main():

    turn = "P1"
    plays = 0
    tabuleiro = {
        "row_1": ["1", "4", "7"],
        "row_2": ["2", "5", "8"],
        "row_3": ["3", "6", "9"]
    }
    choice = ""

    while endgame == False:
        print(display_board(tabuleiro))

        if turn == "P1":
            choice = input("\nPlayer 1 - Choose a position (1-9): ")

            if choice == "1" and tabuleiro["row_1"][0] == "1":
                tabuleiro["row_1"][0] = player_1
            elif choice == "2" and tabuleiro["row_2"][0] == "2":
                tabuleiro["row_2"][0] = player_1
            elif choice == "3" and tabuleiro["row_3"][0] == "3":
                tabuleiro["row_3"][0] = player_1
            elif choice == "4" and tabuleiro["row_1"][1] == "4":
                tabuleiro["row_1"][1] = player_1
            elif choice == "5" and tabuleiro["row_2"][1] == "5":
                tabuleiro["row_2"][1] = player_1
            elif choice == "6" and tabuleiro["row_3"][1] == "6":
                tabuleiro["row_3"][1] = player_1
            elif choice == "7" and tabuleiro["row_1"][2] == "7":
                tabuleiro["row_1"][2] = player_1
            elif choice == "8" and tabuleiro["row_2"][2] == "8":
                tabuleiro["row_2"][2] = player_1
            elif choice == "9" and tabuleiro["row_3"][2] == "9":
                tabuleiro["row_3"][2] = player_1
            else:
                print("\nInvalid choose!")
                input()
                continue

            plays += 1
            check_win(tabuleiro, turn, plays)               
            turn = "P2"
        else:
            choice = input("\nPlayer 2 - Choose a position (1-9): ")
            
            if choice == "1" and tabuleiro["row_1"][0] == "1":
                tabuleiro["row_1"][0] = player_2
            elif choice == "2" and tabuleiro["row_2"][0] == "2":
                tabuleiro["row_2"][0] = player_2
            elif choice == "3" and tabuleiro["row_3"][0] == "3":
                tabuleiro["row_3"][0] = player_2
            elif choice == "4" and tabuleiro["row_1"][1] == "4":
                tabuleiro["row_1"][1] = player_2
            elif choice == "5" and tabuleiro["row_2"][1] == "5":
                tabuleiro["row_2"][1] = player_2
            elif choice == "6" and tabuleiro["row_3"][1] == "6":
                tabuleiro["row_3"][1] = player_2
            elif choice == "7" and tabuleiro["row_1"][2] == "7":
                tabuleiro["row_1"][2] = player_2
            elif choice == "8" and tabuleiro["row_2"][2] == "8":
                tabuleiro["row_2"][2] = player_2
            elif choice == "9" and tabuleiro["row_3"][2] == "9":
                tabuleiro["row_3"][2] = player_2
            else:
                print("\nInvalid choose!")
                input()
                continue

            plays += 1
            check_win(tabuleiro, turn, plays)
            turn = "P1"


if __name__ == "__main__":
    main()