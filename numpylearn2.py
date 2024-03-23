# from FreeCodeCamp.org Data Analysis video segment on numpy module

import numpy as np

# Python is an OOP language, so all numerical values (floats, ints,
# etc.) are class instances, calling the class each time a number is
# stored in RAM-intensive, e.g.
x = 5
# Could be a 3-bit-sized binary object (101) in principle, but Python's
# OOP system makes this value actually size at ~20 bytes (160 bits)
#
# numpy is far more efficient than native Python for math in part b/c
# it allows defining numbers to be a particular size in memory
x = np.int8(5)  # represents 5 as a 1-byte (8-bit) integer

# numpy also optimizes arrays for math efficiency unlike stock Python
# lists. numpy arrays store array values at contiguous memory locations,
# and allow matrix math to be performed by high performance CPU parts.

a = np.array([0, 0.5, 1, 1.5, 2])
b = np.array([1, 2, 3, 4])

# Get values at indices 0, 2, & 4
#
# stock Python way (but also works for numpy):
c = a[0], a[2], a[-1]  # return tuple
# numpy multi-indexing way to get same values:
c = a[[0, 2, -1]]  # returns np.array([0., 1., 2,]) -- easier to use

# np.arrays have types depending on what type a numbers are held within
print(b.dtype)  # dtype('int32') -- detects ints, defaults to 32-bit

# remake b as an array of floats
b = np.array([1, 2, 3, 4], dtype=np.float)  # 1st way via arguments
b = np.array([1., 2., 3., 4.])  # 2nd way; float implied by decimal
print(b.dtype)  # dtype('float64') -- defaults to 64-bit float

# remake b using smaller sized ints
b = np.array([1, 2, 3, 4], dtype=np.int8)

# np.arrays will store numerical objects: ints, floats, Booleans, dates,
# & the like, but not useful for objects (strings, lists, dicts)
print(np.array(['a', 'b', 'c']).dtype)  # dtype('<U1')

# multidimensional np.arrays

# 2-D array
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = a.shape  # returns (2, 3) = (rows, columns); just remember (y, x)
b = a.ndim  # return 2 b/c this is a 2-D array
b = a.size  # returns 6 b/c 6 values in the entire array

# 3-D array
a = np.array([
    [
        # bottom "layer" of 3-D object
        [12, 11, 10],
        [9, 8, 7]
    ],
    [
        [6, 5, 4],
        [3, 2, 1]
    ]
])
b = a.shape  # (2, 2, 3) = (z, y, x)
# this 3-D array is really 2 2x3 matrices stacked on each other
# 4-D array shape is are (w, z, y, x), which is w different (z, y, x)
# cubes hyper-stacked into a hypercube with 4D depth = w

b = a.ndim  # 3
b = a.size  # 12

# Make array where layers are not the same sizes
a = np.array([
    [
        # these 6 values form the 1st of 2 elements in a.size=2
        [12, 11, 10],
        [9, 8, 7]
    ],
    [
        # 3 values form 2nd elements of a.size
        [6, 5, 4]
    ]
])
b = a.dtype  # dtype('O') -- dtype is "Object"
b = a.shape  # (2,) -- 2xNONE object
b = a.size  # =2 -- object made of 2 differently shaped arrays

# axis refers to the direction of movement across the rows, columns,
# etc. Just as np.shape() returns length as (z, y, x), where x indicates
# rows (x ->  across a row). Moving across the rowS (plural) forms a
# downward arrow for axis=0, while moving across the columnS forms a
# rightward arrow, the direction of axis=1. When calling axis, it acts
# in the direction of the axis arrow; while axis=0 points across the
# rows, the arrow is vertical and sums columns, now rows
a = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])
# array([9, 12, 15]) -- column sums since the axis across the rows is a
# vertical (columnar) axis
np.sum(a, axis=0)
# array([3, 12, 21]) -- row sums since the axis across the columns is a
# horizontal (row-like) axis
np.sum(a, axis=1)

# np.concatenate() takes a tuple of 2 np.arrays OF THE SAME SHAPE, and
# an axis. The 2nd array is attached in its printed layout to the right
# or bottom end end of the 1st array. The axis points across 1st array,
# & 2nd array is attached in line with the axis.
a = np.array([
    [0, 1],
    [2, 3],
])
b = np.array([
    [9, 8],
    [7, 6]
])
# axis=0 is vertical, so b is attached to bottom of a (along a vertical
# arrow across a)
print(np.concatenate((a, b), axis=0))
# axis=1 is horizontal, so b is attached to right side of a (along a
# vertical arrow across a)
print(np.concatenate((a, b), axis=1))

# https://github.com/ine-rmotr-curriculum/freecodecamp-intro-to-numpy/
# blob/master/2.%20NumPy.ipynb
