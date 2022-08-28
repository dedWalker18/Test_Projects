# Permutation of lists
# prints all the possible permutations that are not equal to the input n
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

lst = [[x,y,z]]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            lst.append([i,j,k])
lst.pop(0)
print(lst)
ans = []
check = []

for l in range(0,len(lst)):
    check = lst[l]
    if check[0] + check[1] + check[2] != n:
        ans.append(check)

print(ans)
