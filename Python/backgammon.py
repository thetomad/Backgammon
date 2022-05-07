import numpy as np

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

    f_pos = input(f"Your first dice was {dice1}: what position is the chip you want to move to? ")

    f_pos = int(f_pos) -1

   
    if positions[f_pos][1] == turn:
        print("You can move from here.") 
        if positions[f_pos][0] >=0:
            print("You have a peace here.")
            
            if f_pos - dice1 > 0:
                print("The place is on the board")
                if positions[f_pos - dice1][1] == turn or positions[f_pos - dice1][1] == 0:
                    print("The place you end is empty/yours.")
                    positions[f_pos][0] += -1
                    positions[f_pos - dice1][0] += 1

                    if positions[f_pos - dice1][1] == 0:
                        positions[f_pos - dice1][1] = turn


                    if positions[f_pos][0] == 0:
                        positions[f_pos][1] =0

    s_pos = input(f"Your first dice was {dice2}: what position is the chip you want to move to? ")

    s_pos = int(s_pos) -1

   
    if positions[s_pos][1] == turn:
        print("You can move from here.") 
        if positions[s_pos][0] >=0:
            print("You have a peace here.")
            
            if s_pos - dice2 > 0:
                print("The place is on the board")
                if positions[s_pos - dice2][1] == turn or positions[s_pos - dice2][1] == 0:
                    print("The place you end is empty/yours.")
                    positions[s_pos][0] += -1
                    positions[s_pos - dice2][0] += 1

                    if positions[s_pos - dice2][1] == 0:
                        positions[s_pos - dice2][1] = turn


                    if positions[s_pos][0] == 0:
                        positions[s_pos][1] =0


    print(positions)
    

if __name__ == "__main__":
    main()