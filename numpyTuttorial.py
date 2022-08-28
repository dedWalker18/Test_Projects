import numpy as np
lst = [3801,3802,3803,3804]
a = np.array(lst)
b = np.array([49,50,51,52])
for i in range(4):
    print(''.join(str(a[i])),end="    ") #for i in range(4))
print()
print("+ ",end="")
for j in range(4):
    if j == 3:
        print(''.join(str(b[j])))
    else:
        print(''.join(str(b[j])),end="    + ")
for _ in range(4):
    print("-"*5,end="   ")
print()
for l in range(4):
    print(int(a[l]) +int(b[l]),end="    ")

#c = np.array(((1,2,2,3),(5,6,7,8)))
# print(c)
# print(c.ndim)
# print(b.shape)
# print(b.itemsize)
# print(c.nbytes)
# print(b.dtype)
# print(c.dtype)
# print(b)
# print(b)