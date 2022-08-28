import os
import requests

r = requests.get('https://relevel-bucket.s3.amazonaws.com/media/1649426260_da.pdf')
with open('/home/pills/VSCodeProjects/newproject/new.pdf', 'wb') as f:
    f.write(r.content)
