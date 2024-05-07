import os
import time

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_tree(height):
    trunk_width = 3
    for i in range(1, height+1):
        spaces = ' ' * (height - i)
        leaves = '*' * (2*i - 1)
        print(spaces + leaves)
    print(' ' * (height - trunk_width) + '|' * trunk_width)

def grow_tree(height, duration):
    frames = 20
    frame_duration = duration / frames
    for i in range(1, frames+1):
        clear_screen()
        print_tree(int(height * i / frames))
        time.sleep(frame_duration)

def main():
    tree_height = 10
    growth_duration = 10
    print("Growing tree...\n")
    grow_tree(tree_height, growth_duration)
    print("\nTree fully grown!")

if __name__ == "__main__":
    main()