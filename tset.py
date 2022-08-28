# list_org = ['s','d','f','y','4','g']
# list_cp2y = list_org
# list_cp2y.pop()
# print(list_cp2y)
# print(list_org)
#
# new_list = [i+i for i in list_org]
# print(new_list)
#
# tup1 = tuple(new_list)
# tupp2 = (i+i for i in new_list)
# print(tuple(tupp2))
#
#
# my_dict = {"name": "lakshya", "age": 19, "city": "varanasi"}
# my_dict2 = my_dict.copy()
# print(my_dict2)
# print(my_dict)
# new_dict= dict(name= "ayush")
# my_dict2.update(new_dict)
# print(my_dict)
# print(my_dict2)


# Enter your code here. Read input from STDIN. Print output to STDOUT
# import binhex
#import builtins
#import sys
#import re
#import os
#import random
#import math
#import os
#import random
#import re
#import sys

# Enter your code here. Read input from STDIN. Print output to STDOUT
#from collections import namedtuple

# Enter your code here. Read input from STDIN. Print output to STDOUT


# from collections import namedtuple                                                                                    # NAMED TUPLE
#
# N = int(input())
# fields = input().split()
#
# total = 0
# for i in range(N):
#     students = namedtuple('student',fields)
#     field1, field2, field3,field4 = input().split()
#     student = students(field1,field2,field3,field4)
#     total += int(student.MARKS)
# print('{:.2f}'.format(total/N))

# from collections import deque
# d = deque()
# for _ in range(int(input())):
#     inp = input().split()
#     getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
# print(*[item for item in d])                                                                                                      # print every item in any iterable





# from collections import OrderedDict
#
# od = OrderedDict()
# N = int(input())
#
# for i in range(N):
#     *item_words, price = input().split()
#     item = " ".join(item_words)
#
#     if item in od.keys():
#         od[item] += int(price)
#     else:
#         od[item] = int(price)
#
# for item, total in od.items():
#     print(item, total)



# Enter your code here. Read input from STDIN. Print output to STDOUT
# from collections import OrderedDict
#
# n = int(input())
# od = OrderedDict()
#
# for i in range(n):
#     words = input().strip()
#     if words in od.keys():
#         od[words] += int(1)
#     else:
#         od[words] = int(1)
#
#
# print(len(od))
# for j in od:
#     print(od[j], end=" ")

# import calendar
# arr = list(calendar.day_name)
# c,b,a = map(int, input().split())
# s = str(arr[calendar.weekday(a,b,c)-2])
# print(s.upper())


# Enter your code here. Read input from STDIN. Print output to STDOUT

#  import numpy
#
# def arrays(arr):
#     # complete this function
#     # use numpy.array
#     out = numpy.array(arr, float)
#     out1 = numpy.array(float)
#     for i in range(len(out)):
#         out1[0][i] = out[0][-i-1]
#     return out1
#
# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)

#import math
#mport os
#import random
#import re
#import sys

# import numpy
#
#
# def arrays(arr):
#     # complete this function
#     # use numpy.array
#     out = numpy.array(arr, float)
#     out1 = numpy.array(float)
#     a = list(out)
#     b = list(reversed(a))
#     out1.__add__(b)
#     return out1
#
#
# arr = input().strip().split(' ')
# result = arrays(arr)
# print(result)

# regex_pattern = r"[,.]"	# Do not delete 'r'.
#
# import re
# print("\n".join(re.split(regex_pattern, input())))



# n, x = map(int, input().split())                                                                                      # ZIPPED function
# subjects = []
# std = []
# marks = []
# s = 0
# [std.append(i) for i in range(n)]
# #print(std)
# subjects.append([input().split() for j in range(x)])
# for k in range(x):
#    marks.append(list(zip(subjects[0][k],std)))
# #print(marks)
#
# for i in range(n):
#     for l in range(x):
#         s += float(marks[l][i][0])
#     print("{:.1f}".format(s/x))
#     s= 0


# cube = lambda x: x * x * x
# def fibonacci(n):
#     lst = [0, 1]
#     for i in range(2, n):
#         lst.append(int(lst[i-1]) + int(lst[i-2]))
#
#     return lst
#
# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))


# #Code
# t =int(input().strip())
# for i in range(t):
#     try:
#         a, b = map(int, input().split())
#         print(float(a/b))
#     except ZeroDivisionError:
#         print("Error Code: integer division or modulo by zero")
#     except ValueError:
#         print("Error Code: invalid literal for int() with base 10:" + str(b))


# import antigravity


# class Person:
#     def __init__(self, firstName, lastName, idNumber):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.idNumber = idNumber
#
#     def printPerson(self):
#         print("Name:", self.lastName + ",", self.firstName)
#         print("ID:", self.idNumber)
#
#
# #max = 0
#
#
# class Student(Person):
#     #   Class Constructor
#     #global max
#     #max = 0
#     def __init__(self, firstName, lastName, idNum, scores):
#         #   Parameters
#         self.firstName = firstName
#         self.idNumber = idNum
#         self.lastName = lastName
#         self.scores = scores
#
#     # Write your constructor here
#     def calculate(self):
#         max = 0
#         for i in range(numScores):
#             max += scores[i]
#         max = int(max / numScores)
#         if 90 <= max <= 100:
#             ans ="O"
#             return ans
#         elif 80 <= max < 90:
#             ans ="E"
#             return ans
#         elif 70 <= max < 80:
#             ans ="A"
#             return ans
#         elif 55 <= max < 70:
#             ans ="P"
#             return ans
#         elif 40 <= max < 55:
#             ans ="D"
#             return ans
#         elif max < 40:
#             ans ="T"
#             return ans
#             #   Function Name: calculate
#     #   Return: A character denoting the grade.
#     #
#     # Write your function here
#
#
# line = input().split()
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]
# numScores = int(input())  # not needed for Python
# scores = list(map(int, input().split()))
# s = Student(firstName, lastName, idNum, scores)
# s.printPerson()
# print("Grade: "+ s.calculate())


# from abc import ABCMeta, abstractmethod                                                                                ABSTRACTION
# class Book(object, metaclass=ABCMeta):
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     @abstractmethod
#     def display(): pass
#
# #Write MyBook class
# class MyBook(Book):
#     def __init__(self,title,author,price):
#         self.title = title
#         self.author = author
#         self.prive = price
#     def display(self):
#         print("Title:",title)
#         print("Author:",author)
#         print("Price:",price)
#
# title=input()
# author=input()
# price=int(input())
# new_novel=MyBook(title,author,price)
# new_novel.display()



# import numpy as np
# n, m = map(int, input().split())
# lst = []
# for i in range(n):
#     lst.append(list(map(int, input().split())))
# arr = np.array(lst)
# print(arr.transpose())
# print(arr.flatten())



# import numpy
#
# lst = list(map(int, input().split()))
# print(numpy.zeros([*lst],dtype = numpy.int))
# print(numpy.ones([*lst],dtype = numpy.int))



# import numpy
#
# numpy.set_printoptions(legacy="1.13")
#
# lst = map(int, input().split())
# print(numpy.eye(*lst))