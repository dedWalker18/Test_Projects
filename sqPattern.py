len_sq = int(input("Enter the length of Each side of Square: "))                                                        # Input
br_sq = len_sq
mem = len_sq

while len_sq > 0:                                                                                                       # Loop for nummber of lines
    while br_sq > 0:                                                                                                    # Loop for each line
        print("#  ", end="")
        br_sq = br_sq - 1
    len_sq = len_sq - 1                                                                                                 # Resetting Variables
    br_sq = mem
    print("")
# END