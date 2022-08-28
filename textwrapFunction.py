import textwrap

i = input()
max_width = int(input())
ot = '\n'.join(textwrap.wrap(i, max_width))
print(ot)