len_str = int(input("Enter the length of stairs: "))                                                                    # Input
mem = len_str

while mem > 0:                                                                                                          # Loop for number of steps
    while len_str > 0:                                                                                                  # Loop for each step
        print("# ", end="")
        len_str -= 1
    mem -= 1                                                                                                            # Resetting Variables
    len_str = mem
    print("")

# END