import random                                                                                                           #Random Package Imported

x = int(input("Enter the starting value: "))                                                                            #Input Range from user
y = int(input("Enter the end value: "))

ran_num = random.randint(x, y)

guess = int(input("Enter your first Guess, 5 chances remain: "))                                                        # First Guess

chances = 5
win = False

while 5 >= chances >= 2:                                                                                                #Body
    if guess == ran_num:
        win = True
        break
    elif guess < ran_num:
        chances -= 1
        print("Keep Trying Higher, {} chances Remain".format(chances))
        guess = int(input("Enter your guess: "))
    elif guess > ran_num:
        chances -= 1
        print("Keep Trying Lower, {} chances Remain".format(chances))
        guess = int(input("Enter you guess: "))

if chances == 1:                                                                                                        #Declaration
    print("You Lost")
if win == True:
    print("You Won")

# END