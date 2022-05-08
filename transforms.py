import numpy as np

def partition(arr):
    return np.block([[             arr, np.zeros((3, 3))], 
                     [np.zeros((3, 3)),   np.identity(3)]])

scale = lambda s: partition(np.array([[s, 0, 0],
                                      [0, s, 0],
                                      [0, 0, 1]]))

move = lambda x, y: partition(np.array([[1, 0, x],
                                        [0, 1, y],
                                        [0, 0, 1]]))

project = partition(np.array([[1, 0, 0],
                              [0, 0, 0],
                              [0, 0, 1]]))

reflect1 = partition(np.array([[1, 2, 0],
                               [0, 1, 0],
                               [0, 0, 1]]))

rotation = lambda theta: partition(np.array([[ np.cos(theta),-np.sin(theta), 0], 
                                             [ np.sin(theta), np.cos(theta), 0],
                                             [             0,             0, 1]]))

shearexample = partition(np.array([[1, 1, 0],
                                   [0, 1, 0],
                                   [0, 0, 1]]))

shear1 = lambda theta: partition(np.array([[1,   -np.tan(theta/2), 0],
                                           [0,                  1, 0],
                                           [0,                  0, 1]]))
shear2 = lambda theta: partition(np.array([[            1, 0, 0],
                                           [np.sin(theta), 1, 0],
                                           [0,             0, 1]]))
shear3 = lambda theta: partition(np.array([[1,   -np.tan(theta/2), 0],
                                           [0,                  1, 0],
                                           [0,                  0, 1]]))

colorshift1 = np.array([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0.25, 0],
    [0, 0, 0, 0, 0, 0.25]
])

colorshift2 = np.array([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [-0.1, 0, 0, 0, 1, 0],
    [-0.1, 0, 0, 0, 0, 1]
])

#rgb = 