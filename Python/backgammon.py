import numpy as np


def p_moves(dice, positions, turn, p_out):
    
    
    if turn == 1:
        fin_pos = f_pos - dice
        a_turn =-1
        out = p_out[1]
    else: 
        fin_pos = f_pos + dice
        a_turn =1
        out = p_out[0]

    if out[0] == 0:
        f_pos = input(f"Your dice was {dice}: what position is the piece you want to move to? ")

        f_pos = int(f_pos) -1

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

                    p_out += 1

                else:
                    print("Ocupied place!")
            else:
                print("Outside the board!")
        else:
            print("No pieces of yours here")

        print(positions)
        print("\n")
        return
    else:
        if turn == 1:
            if positions[24 - dice][1] != a_turn:
                positions[24-dice][0] += 1
                positions[24 - dice ][1] +=1
            elif positions[ 24 - dice ] == 1:

                positions[ 24 - dice ][1] = turn
                p_out[0][0] += 1
            else:
                print("you can't to this cause it's ocupied")
        elif turn == -1:
            if positions[dice - 1][1] != a_turn:
                positions[dice - 1][0] += 1
                positions[dice - 1][1] +=1
            elif positions[dice - 1] == 1:

                positions[dice - 1 ][1] = turn
                p_out[1][0] += 1
            else:
                print("you can't to this cause it's ocupied")
    

def create_board():
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
    
    turn = 1
    
    p_out = [[0,-1],[0,1]]
    
    return positions, turn, p_out

def turn_end(turn):
    if turn == 1:
        turn = -1
    else:
        turn == 1

def main():
    
    # creating the board
    positions, turn, p_out = create_board()


    # create dices
    dice1 = np.random.randint(1,7)
    dice2 = np.random.randint(1,7)

    print(f"Your dices were {dice1} and {dice2}. \n")

    #pieces move
    p_moves(dice1, positions, turn, p_out)
    p_moves(dice2, positions, turn, p_out)

    # turn ends
    turn_end()
    
    

if __name__ == "__main__":
    main()