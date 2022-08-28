import random
import numpy as np
import math
from PIL import Image, ImageDraw
import cmath
print("Starting")





# Constants - Be careful it is easy to throw the image off editing these.
NumberOfIterationsPerPoint = 10
Interval = 5
size = 1
WindowSize = 400
scale = Interval / WindowSize
blewup = 0

im = Image.new('RGB', (WindowSize, WindowSize))

# Loop going over the number of points
for i in range(WindowSize):
    for j in range(WindowSize):
        # Make a staring point
        x0 = scale * (i - 0.5 * WindowSize) + scale * (j - 0.5 * WindowSize) * 1j


        # Create the iterate function
        def interate(x):
            # This is the imput function and editing it is probably the coolest way to make new pictures.  Right now it is using the function x^2+x0 for the mandelbrat set.  You can make cool new fractals by making this any function of x and x0
            return (math.pow(x.real, 2) - math.pow(x.imag, 2) + 2 * x.real * x.imag * 1j) + x0


        # Iterate the function
        for N in range(NumberOfIterationsPerPoint):
            blewup = 0
            if (N == 0):
                # This is the inital condition of the fractal.  You can make cool fratals like Julia Sets by editing this.
                x = 0
            elif (abs(x) < 2):
                x = interate(x)
            else:
                blewup = 1

        # Make an image iterator
        imiter = ImageDraw.Draw(im)

        # Determine the shade of the point and plot it
        xr = abs(x.real)
        xi = abs(x.imag)
        mod = abs(x)
        x0r = x0.real / scale + 0.5 * WindowSize
        x0i = x0.imag / scale + 0.5 * WindowSize

        if (blewup == 1):
            imiter.ellipse([(x0r, x0i), (x0r + size, x0i + size)], (200, 100, 100))

        else:
            imiter.ellipse([(x0r / scale, x0i), (x0r + size, x0i + size)], (0, 0, 0))

        if (i < 0.25 * WindowSize):
            print("Staring Drawing")
        elif (i < 0.5 * WindowSize):
            print("Almost Half Way There")
        elif (i < 0.75 * WindowSize):
            print("Half Way There")
        else:
            print("Almost Done")




im.save("fractal.jpg")