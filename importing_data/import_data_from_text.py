
import numpy as np

data = np.genfromtxt("mydata.txt")                       # mydata.txt contains 4 columns of numbers

t,z = data[:,0], data[:,3]                                    # data is 2D numpy array
t,x,y,z = np.genfromtxt("mydata.txt", unpack=True,delimiter=',',dtype=float)                  # to unpack all columns

t,z     = np.genfromtxt("mydata.txt", usecols = (0,3),dtype=float, unpack=True)     # to select just a few columns
print('Import columns 0 and 3')
print(t,z)

data    = np.genfromtxt("mydata.txt", dtype=float)                    # to skip 2 rows from top of file
print('Import all data as float type')
print(data)

data    = np.genfromtxt("mydata.txt", comments = '#',dtype=float)                  # use '#' as comment char
print('Ignore Comment lines starting with #')
print(data)

