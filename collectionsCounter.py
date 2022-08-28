# >>> from collections import Counter
# >>>
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>>
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>>
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]

from collections import Counter
N = int(input())
n = input().split()
C = int(input())
c1 = {}
c2 = {}
for i in range(0, C):
    c1[i], c2[i] = input().split()
stock = Counter(n)
demand = Counter(c1.values())
price = Counter(c2.values())
#print(stock['6'])
#print(c1)
#print(c2)
#print(demand)
#print(price)
revenue = 0

for a in range(0, len(c1)):
    now = str(c1[a])
    if stock[now] > 0:
        revenue = revenue + int(c2[a])
        stock[now] -= 1

print(revenue)