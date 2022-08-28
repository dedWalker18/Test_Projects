import math
n, m = input().split()
n = int(n)
m = int(m)


# for j in range(1,m+1):
j = 1
while j <= (m-6)/3:
    text = ".|." * j
    print(text.center(m,"-"))
    j = j + 2

print("WELCOME".center(m,"-"))

k=int((m-6)/3)
while k > 0:
    text = ".|." * k
    print(text.center(m, "-"))
    k = k -2