import numpy as np

# create list
x = np.array([2, 3, 4])
print(x)

# np.arange(x,y) works like Python range(x,y): it creates a list of
# from x to y-1. y is always excluded. Like Python range(y),
# np.arange(y) is treated like np.arange(0,y) and creates a list of
# values from 0 to y-1 (although len(np.arange(y)) = y).

# create list of digits from 0-11
x = np.arange(12)  # np.arange(0, 12) is identical
# create list of digits from 1-11
x = np.arange(1, 12)

# create list of digits from 0-10 by 2s; does NOT include 12
x = np.arange(0, 12, 2)  # [0, 2, 4, 6, 8, 10]
print(x)

# Indexing:
#       - a[x] gives x-th item in array
#       - a[x:y] give array of a from a[0] to a[y-1]
#       - a[x:] gives array from a[x] to a[-1]
#       - a[:x] gives array from a[0] to a[y-1]
#       - a[x:y:z] gives every z-th item from a[x] to a[y-1]
#               - technically last value is a[y - (y % z)]
#       - a[:y:z] is every z-th value from a[0] to a[y - (y % z)]
#       - a[x::z] is every z-th value from a[x] to a[a[-1] - (a[-1]%z)]
#       - a[::z] is every z-th value from a[0] to a[a[-1] - (a[-1]%z)]
#       - a[x::] = a[x:]
#       - a[:y:] = a[:y] = a[0:y]
#       - a[::] = a[0:-1]

# create list of 6 evenly spaced element from 1-12
x = np.linspace(1, 12, 6)
print(x)

# reshape array into 3x2 = 3 rows/sublists, 2 columns/items per sublist
x.reshape(3, 2)
print(x)

y = x.size  # number of elements in array
print(y)

y = x.shape  # returns (rows, columns)
print(y)

y = x.dtype   # returns type of data used to store elements
print(y)
y = x.itemsize  # returns #bytes taken by each element
print(y)

# create 2-D array
x = np.array([
        [1.5, 2, 3],
        [4, 5, 6]
])

# create array of same dimensions with Booleans for each element based
# on whether element < 4
y = (x < 4)
print(y)

# multiply each element by 3
x *= 3
print(x)
y = x*3
print(y)

# create 3x4 array of zeroes
x = np.zeros((3, 4))
print(x)

# create 3x4 array of ones
x = np.ones((3, 4))
print(x)

# create 1-D array (list) of 10 ones
x = np.ones(10)
print(x)

# create 1-D array using 16-bit floats (default = 64) conserves memory
x = np.array([2, 3, 4], dtype=np.int16)
print(x)

# create 2x3 of random float64 values from 0-1
np.random.random((2, 3))
print(x)

# set print preferences to 2 decimals, a suppress scientific notation
np.set_printoptions(precision=2, suppress=True)

# create 1-D array of 5 random integers from 0-10
np.random.randint(0, 10, 5)

# math fxns
y = x.sum()  # sum of all elements
print(y)
y = x.min()  # minimum value
print(y)
y = x.max()  # max value
print(y)
y = x.mean()  # mean of elements
print(y)
y - x.var()  # variance of elements
print(y)
y = x.std()  # std deviation of elements
print(y)

# give sum of each column in array of 3x2 (rows, columns)
x = np.random.randint(0, 10, 6)
x = x.reshape((3, 2))
y = x.sum(axis=0)
print(x)
print(y)

# create array of [rows, columns] whose values are a random sample from
# the Gaussian distribution w/ mu = mean & sigma = S.D., stated formally
# as the N(mu, sigma**2) distribution.
rows = 2
columns = 4
mu = 100
sigma = 15
# create 2x4 matrix of IQ score dist samples, where dist is N(100, 225)
iq_sample = mu + sigma * np.random.randn(rows, columns)

# give sum of each row
y = x.sum(axis=1)
print(y)

# can call axis for any of the math fxns


# get data.txt csv as unsigned 8-bit integers, skip 1st row (header row)
# x = np.loadtxt('data.txt', dtype=np.uint8, delimiter=',', skiprows=1)
# print(x)

# create list of values from 0-9, then shuffle the order
x = np.arange(10)
np.random.shuffle(x)
print(x)

# randomly return 1 element from list
np.random.choice(x)


