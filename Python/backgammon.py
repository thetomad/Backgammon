import numpy as np


def p_moves(dice, positions, turn):
    f_pos = input(f"Your dice was {dice}: what position is the piece you want to move to? ")

    f_pos = int(f_pos) -1

    if turn == 1:
        fin_pos = f_pos - dice
        a_turn =-1
    else: 
        fin_pos = f_pos + dice
        a_turn =1


    if positions[f_pos][1] == turn:
        if fin_pos > 0 and fin_pos <25:
            if positions[fin_pos][1] != a_turn:
                
                positions[f_pos][0] += -1
                positions[fin_pos][0] += 1

                if positions[fin_pos][1] == 0:
                    positions[fin_pos][1] = turn


                if positions[f_pos][0] == 0:
                    positions[f_pos][1] = 0

            elif positions[fin_pos][0] == 1:
                
                positions[fin_pos][1] = turn

                positions[f_pos] += -1

                if positions[f_pos][0] == 0:
                    positions[f_pos][1] = 0

            else:
                print("Ocupied place!")
        else:
            print("Outside the board!")
    else:
        print("No pieces of yours here")



def main():
    positions = []

    for i in range(24):
        new_pos = [0, 0]
        positions.append(new_pos)

    # create initial position

    positions[0] = [2, -1]
    positions[5] = [5, 1]
    positions[7] = [3, 1]
    positions[11] = [5, -1]
    positions[12] = [5, 1]
    positions[16] = [3, -1]
    positions[18] = [5, -1]
    positions[23] = [2, 1]
    
    
    for i in range(24):
        print(f"{positions[i]}  --  pos{i + 1}")

    # create turn order

    turn = 1

    # create dices

    dice1 = np.random.randint(1,7)
    dice2 = np.random.randint(1,7)

    print(f"Your dices were {dice1} and {dice2}. \n")


    #pieces move
    p_moves(dice1, positions, turn)
    p_moves(dice2, positions, turn)

    # turn ends
    if turn == 1:
        turn = -1
    else:
        turn == 1

    print(positions)
    

if __name__ == "__main__":
    main()