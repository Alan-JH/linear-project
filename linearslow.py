import numpy as np 
from PIL import Image, ImageDraw
import sys
import math, time

sttime = time.perf_counter()
vec_round = np.vectorize(round)

name = sys.argv[1]
img = Image.open(name)
numpydata = np.asarray(img)

theta = 30 * math.pi / 180
rotation = np.array([[ np.sin(theta), np.cos(theta), 0], # Matrix transform
                    [ np.cos(theta), np.sin(theta), 0],
                    [ 0, 0, 1]])

result = np.ones([3000, 3000, 3]) * 255 # Create a white canvas

for i in range(len(numpydata)):
    for j in range(len(numpydata[i])): # For each element of old image, calculate new x and y for transformed image
        val = numpydata[i, j]
        x = np.array([i, j, 1])
        xprime = vec_round(rotation.dot(x))
        #print(xprime)
        result[xprime[0], xprime[1]] = val

PIL_image = Image.fromarray(result.astype('uint8'), 'RGB')
PIL_image.save('result.png') # Save image
print(time.perf_counter()-sttime)