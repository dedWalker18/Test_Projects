len_stairs = int(input("Enter the number of ssteps on stair: "))                                                        # Input
i = 1
j = 0

while len_stairs > 0:                                                                                                   # Loop for number of steps
    while j < i:                                                                                                        # Loop for each steps
         print("* ", end="")
         j += 1
    i += 1                                                                                                              # Resetting Variables
    j = 0
    len_stairs -= 1
    print("")

# END