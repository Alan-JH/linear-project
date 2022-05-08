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

def img_to_matrix(npdata):
    i = np.arange(npdata.shape[0])
    j = np.arange(npdata.shape[1])
    out = np.empty((npdata.shape[0], npdata.shape[1], 6),dtype=int)
    out[:,:,0] = i[:,None] # Column vector
    out[:,:,1] = j # Row vector
    out[:,:,2] = 1
    out[:,:,3:] = npdata[i[:,None], j]
    return out.reshape(-1, out.shape[-1]).T

def matrix_to_img(npdata):
    arr = np.ones([2700, 2700, 3]) * 255 # Create a white canvas
    npdata = vec_round(npdata)
    arr[npdata[0], npdata[1]] = npdata[3:].T
    return arr

data = img_to_matrix(numpydata)

images = []
for i in range(0, 360, 10):
    theta = i * math.pi / 180
    # Matrix transform x, y, 1, r, g, b
    transformation = transforms.rotation(theta)

    result = matrix_to_img(transforms.move(1250, 1250).dot(transformation).dot(data))

    PIL_image = Image.fromarray(result.astype('uint8'), 'RGB')
    images.append(PIL_image)

images[0].save('result.gif', save_all=True, append_images=images[1:], optimize=False, duration=200, loop=0)
print(time.perf_counter()-sttime)