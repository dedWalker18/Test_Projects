#input course, prerequisites, corequisites
#output all the ways i can take courses

from distutils import core
from http.client import CannotSendRequest
import itertools
from more_itertools import first
from itertools import *


def num_of_ways(a, b, c, d):
    course_left = a
    courses_completed = b
    prerequisites = c
    corequisites = d
    ways = []
    terms = list(itertools.combinations(course_left, r=3))
    copy = terms
    for term in terms:
        for course in term:
            if course not in corequisites:
                continue
            elif corequisites[course] in term:
               continue
            else:
                if term in copy:
                    copy.remove(term)
                
    return copy
            
                
course = ["MLF", "MAD2", "BDM", "MLT", "MLP", "BA", "TDS"]

courses_completed = ["PDSA", "MAD1", "DBMS", "JAVA", "SC"]

prerequisites = {"MAD2" : "MAD1",
                 "MLT" : "MLF",
                 "MLP" : "MLF",
                 "BA" : "BDM"}

corequisites = {"MLP" : "MLT",
                "MLT" : "MLP",
                "TDS" : "BA",
                "BA" : "TDS"}

print(num_of_ways(course, courses_completed, prerequisites, corequisites))