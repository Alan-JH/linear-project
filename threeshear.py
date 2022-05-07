import numpy as np 
from PIL import Image, ImageDraw
import sys
import math, time
from transforms import move, shear1, shear2, shear3, rotation

sttime = time.perf_counter()
vec_round = np.vectorize(round)

name = sys.argv[1]
img = Image.open(name)
numpydata = np.asarray(img)

theta = 35 * math.pi / 180
# Matrix transform x, y, 1, r, g, b


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

#data = vec_round(move(1000, 1000).dot(img_to_matrix(numpydata)))
data = img_to_matrix(numpydata)

#raw = vec_round(move(1000, 1000).dot(data))
raw = data
result1 = vec_round(shear1(theta).dot(raw))
result2 = vec_round(shear2(theta).dot(result1))
result3 = vec_round(shear3(theta).dot(result2))

img0 = Image.fromarray(matrix_to_img(vec_round(move(1000, 1000).dot(raw))).astype('uint8'), 'RGB')
img1 = Image.fromarray(matrix_to_img(vec_round(move(1000, 1000).dot(result1))).astype('uint8'), 'RGB')
img2 = Image.fromarray(matrix_to_img(vec_round(move(1000, 1000).dot(result2))).astype('uint8'), 'RGB')
imgfinal = Image.fromarray(matrix_to_img(vec_round(move(1000, 1000).dot(result3))).astype('uint8'), 'RGB')

img0.save('original.png')
img1.save('shear1.png') # Save image
img2.save('shear2.png')
imgfinal.save('shear3.png')

singletrans = matrix_to_img(vec_round(move(1000, 1000).dot(rotation(theta)).dot(raw)))
Image.fromarray(singletrans.astype('uint8'), 'RGB').save('rotationmatrix.png')
print(time.perf_counter()-sttime)
