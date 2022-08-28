# insert i e: Insert integer i at position e.
# print: Print the list.
# remove e: Delete the first occurrence of e integer .
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

if __name__ == '__main__':
    N = int(input())
lst = []
lst1 = []
for i in range(0,N):
    lst.append(input().split())

for j in range(0,N):
      if lst[j][0] == "insert":
          lst1.insert(int(lst[j][1]),int(lst[j][2]))
      elif lst[j][0] == "print":
          print(lst1)
      elif lst[j][0] == "remove":
          lst1.remove(int(lst[j][1]))
      elif lst[j][0] == "append":
          lst1.append(int(lst[j][1]))
      elif lst[j][0] == "sort":
          lst1.sort()
      elif lst[j][0] == "pop":
          lst1.pop()
      elif lst[j][0] == "reverse":
          lst1.reverse()

