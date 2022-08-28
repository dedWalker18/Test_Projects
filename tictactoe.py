print("GameBoard    Positions")
for r in range(0, 9, 3):
    print("- | - | -    " + str((r+1)) + " | " + str((r+2)) + " | " + str((r+3)))


def check(dic):
    x = "X"
    o = "0"
    emd_game = 0
    if dic[0] == dic[1] == dic[2] == x:
        print(" \n X Won")
        emd_game = 1
    elif dic[3] == dic[4] == dic[5] == x:
        print(" \n X Won")
        emd_game = 1
    elif dic[6] == dic[7] == dic[8] == x:
        print(" \n X Won")
        emd_game = 1
    elif dic[0] == dic[3] == dic[6] == x:
        print(" \n X Won")
        emd_game = 1
    elif dic[1] == dic[4] == dic[7] == x:
        print(" \n X Won")
        emd_game = 1
    elif dic[2] == dic[5] == dic[8] == x:
        print(" \n X Won")
        emd_game = 1
    elif dic[0] == dic[4] == dic[8] == x:
        print(" \n X Won")
        emd_game = 1
    elif dic[2] == dic[4] == dic[6] == x:
        print(" \n X Won")
        emd_game = 1
    elif dic[0] == dic[1] == dic[2] == o:
        print(" \n 0 Won")
        emd_game = 1
    elif dic[3] == dic[4] == dic[5] == o:
        print(" \n 0 Won")
        emd_game = 1
    elif dic[6] == dic[7] == dic[8] == o:
        print(" \n 0 Won")
        emd_game = 1
    elif dic[0] == dic[3] == dic[6] == o:
        print(" \n 0 Won")
        emd_game = 1
    elif dic[1] == dic[4] == dic[7] == o:
        print(" \n 0 Won")
        emd_game = 1
    elif dic[2] == dic[5] == dic[8] == o:
        print(" \n 0 Won")
        emd_game = 1
    elif dic[0] == dic[4] == dic[8] == o:
        print(" \n 0 Won")
        emd_game = 1
    elif dic[2] == dic[4] == dic[6] == o:
        print(" \n 0 Won")
        emd_game = 1
    return emd_game

poss1 = {}
poss = {}
for q in range(1, 10):
    poss[q-1] = str(q)
poss1 = {}
for q1 in range(0,9):
    poss1[q1] = str("-")
for j in range(0, 9):
    if j.__mod__(2) == 0:
        print('\n'"X's Turn")  # X turn
        inpx = int(input("Enter Position: "))
        if 0 < inpx < 10:
            poss[inpx - 1] = "X"
            poss1[inpx - 1] = "x"
            print("GameBoard     Positions")
            for first in range(0, 9, 3):
                print(poss1[first] + " | " + poss1[first+1] + " | " + poss1[first+2], end="     ")
                print(str((first + 1)) + " | " + str((first + 2)) + " | " + str((first + 3)))
        else:
            print("Error, Restart!")
            break
        out = check(poss)
        if out == 1:
            break
    else:
        print('\n'"0's Turn")  # 0 turn
        inpy = int(input("Enter Position: "))
        if 0 < inpy < 10:
            poss[inpy - 1] = "0"
            poss1[inpy - 1] = "0"
            print("GameBoard     Positions")
            for second in range(0, 9, 3):
                print(poss1[second] + " | " + poss1[second + 1] + " | " + poss1[second + 2], end="     ")
                print(str((second + 1)) + " | " + str((second + 2)) + " | " + str((second + 3)))
        else:
            print("Error, Restart!")
            break
        out1 = check(poss)
        if out1 == 1:
            break

if out == out1 == 0:
    print("\n   Nobody Wins")
