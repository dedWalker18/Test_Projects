import PIL
from PIL import Image
from tkinter.filedialog import *

filepath = askopenfilename()
img = PIL.Image.open(filepath)
myheight, mywidth = img.size

img = img.resize((myheight, mywidth), PIL.Image.ANTIALIAS)
save_path = askopenfilename()

img.save(save_path+"_compressed.JPG")

