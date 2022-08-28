from email import header
import os
import requests

# print(os.listdir())

f1 = requests.get('https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt')
f2 = requests.get('https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt')
f3 = requests.get('https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt')

"""
with open('/home/pills/VSCodeProjects/newproject/loans1.txt', 'wb') as f:
    f.write(f1.content)

with open('/home/pills/VSCodeProjects/newproject/loans2.txt', 'wb') as f:
    f.write(f2.content)
    
with open('/home/pills/VSCodeProjects/newproject/loans3.txt', 'wb') as f:
    f.write(f3.content)
    
with open('/home/pills/VSCodeProjects/newproject/loans2.txt', 'r') as f:
    print(f.read())
"""

def parse_headers(header_line):
    return header_line.strip().split(',')

"""
with open('/home/pills/VSCodeProjects/newproject/loans1.txt', 'r') as f:
    print(parse_headers(f.readlines()[0]))
"""

def parse_values(data_lines):
    values = []
    for item in data_lines.strip().split(','):
        try:
            values.append(float(item))
        except ValueError:
            values.append(0.0)
    return values

"""
with open('/home/pills/VSCodeProjects/newproject/loans2.txt', 'r') as f:
    print(parse_values(f.readlines()[1]))
"""

def create_item_dict(values, headers):
    result = {}
    for value, header in zip(values, headers):
        result[header] = value
    return result

def read_csv(path):
    result = []
    with open(path, 'r') as f:
        lines = f.readlines()
        headers = parse_headers(lines[0])
        for data_line in lines[1:]:
            values = parse_values(data_line)
            item_dict = create_item_dict(values, headers)
            result.append(item_dict)
    return result

print(read_csv('./loans2.txt'))