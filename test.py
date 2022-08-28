# import math

# (lambda n, apply: [print(''.join(apply(input()))) for _ in range(n)    ]   )(   int(input()), lambda x : [x[i] for i in range(0, len(x), 2)] + [' '] + [x[i] for i in range(1, len(x), 2)]   )

fhand = open('testText.txt')
print(fhand)

counts = { 'quincy' : 10 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))

d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items():
    print(k, i)

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)

import cmath
z = complex(input())
p = cmath.polar(z)
print(p[0])
print(p[1])