def print_rangoli(size):
    # your code goes here
    for i in range(-size + 1, size):
        print("--" * abs(i), end="")
        for j in range(size, abs(i) + 1, -1):
            print(chr(96 + j), end="-")
        print(chr(97 + abs(i)), end="")
        for j in range(abs(i) + 1, size):
            print("-", chr(97 + j), end="", sep="")
        print("--" * abs(i), end="")
        print()


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)