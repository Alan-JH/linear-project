import numpy as np 
from PIL import Image, ImageDraw
import sys
import math, time
import transforms

sttime = time.perf_counter()
vec_round = np.vectorize(round)

name = sys.argv[1]
img = Image.open(name)
numpydata = np.asarray(img)
numpydata = np.swapaxes(numpydata,0,1) # convert row column to xy

theta = 180 * math.pi / 180
# Matrix transform x, y, 1, r, g, b
#transformation = transforms.rotation(theta)
#transformation = transforms.shearexample
transformation = transforms.colorshift2

def img_to_matrix(npdata):
    i = np.arange(npdata.shape[0])
    j = np.arange(npdata.shape[1])
    out = np.empty((npdata.shape[0], npdata.shape[1], 6),dtype=int)
    out[:,:,0] = i[:,None] # Column vector
    out[:,:,1] = j # Row vector
    out[:,:,2] = 1
    out[:,:,3:] = npdata[i[:,None], j]
    return out.reshape(-1, out.shape[-1]).T

def img_to_matrix_slow(npdata):
    #Slow implementation:
    arr = []
    for i in range(len(npdata)):
        for j in range(len(npdata[0])):
            val = npdata[i, j]
            arr.append([i, j, 1, *val])
    return np.array(arr).T

def matrix_to_img(npdata):
    arr = np.ones([3000, 3000, 3]) * 255 # Create a white canvas
    npdata = vec_round(npdata)
    arr[npdata[0], npdata[1]] = npdata[3:].T
    return arr

def matrix_to_img_slow(npdata):
    #Slow implementation:
    arr = np.ones([3000, 3000, 3]) * 255 # Create a white canvas
    for i in npdata:
       i = vec_round(i)
       arr[i[0], i[1]] = i[3:]
    return arr

data = img_to_matrix(numpydata)

result = matrix_to_img(transformation.dot(data))
result = np.swapaxes(result,0,1) # convert xy to row column


PIL_image = Image.fromarray(result.astype('uint8'), 'RGB')
PIL_image.save('result.png') # Save image
print(time.perf_counter()-sttime)
