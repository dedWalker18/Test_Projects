n = int(input("Enter value of N: "))
for i in range(-n+1, n):
    for j in range(n, abs(i), -1):
        print(j, end=" ")
    print((str(abs(i)+1)+" ")*(2*abs(i)), end="")
    for k in range(abs(i)+2, n+1):
        print(k, end=" ")
    print()
    