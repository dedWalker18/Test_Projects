i, out = 1, 1
def factorial(n):
    global i, out
    if i < n+1:
        out = out * i
        i += 1
        factorial(n)

    return out

print(factorial(5))

