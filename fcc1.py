import math

lst = list(map(int, input().split()))

if len(lst).__mod__(2) == 0:
    i = int(len(lst)/2)
else:
    i = int(math.ceil(len(lst)/2))

for j in range(int(math.log(len(lst), 2))):
    if lst[i] >= lst[i+1] and lst[i] >= lst[i-1]:
        print(lst[i])
        #print(i)
        break