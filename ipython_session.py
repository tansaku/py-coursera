# Machine learning class (sort of ...)
# iPython tutorial 

# note full script of the Octave tutorial now available here: https://share.coursera.org/wiki/index.php/ML:Octave_Tutorial

# =======================================================
# Section 1: iPython Tutorial: Basic operations

# elementary operations

5+6
3-2
5*8
1/2. # note need for floating point specification - can fix via 'from __future__ import division'
2**6 # raising to power is ^ in Octave
1 == 2  # false
1 != 2  # true.  note, not "~="
1 and 0 and 2.0 # False --> shortcircuits
#1 & 0 & 2.0 # returns an error because can't compare int and float bit-wise
1 and 0 and 2.0
1 or 0
1 | 0 # bitwise/logical or
1 | 0 | -5 # outputs -5
1 or 0 or -5 # outputs 1
1 ^ 0 # this is bitwise XOR in python


## variable assignment
a = 3; # note that semi-colon ';' is not required in python and has no effect except to allow multiple statements on one line
b = 'hi'
c = 3 >= 1
d = 4

# Displaying them:
a = pi
print '2 decimals: %0.2f' % a # note use of % instead of , as in Octave
print '6 decimals: %0.6f' % d
print '2 decimals: %0.2f and 6 decimals: %0.6f' % (a, d) # for multiple need to use parentheses


# Octave's global formatting not supported in Python - would have to import Decimal and even then things a bit sticky
# format long
# format short
# (actually, there *is* a way to change the *display* format, just blanking on it at the moment)


#  vectors and matrices

#PKHG you forgot to to import np or from ... import numpy as * ???
# SRHJ doesn't seem to be required in my enthought distribution - is already pre-imported I believe


A = array([[1, 2], [3, 4], [5, 6]])  # Octave was A = [1 2; 3 4; 5 6]
# would be nice if numpy had a pretty print option for arrays that we could turn on by default ...

v = hstack((1,2,3))        # Octave was v = [1 2 3]
v = vstack((1,2,3))  #  Octave was v = [1; 2; 3] -- vstack takes a tuple of arrays (or single values in this case
v = linspace(1, 2, 11)   # from 1 to 2, with stepsize of 0.1. Useful for plot axes?  this was v = [1:0.1:2]
v = arange(1,7)        # from 1 to 7 exclusive, assumes stepsize of 1.  this was v = 1:6

q = ones([5, 3, 2]) # multidimensional array


C = 2 * ones([2,3])  # same as C = [[2 2 2],[2 2 2]] (NOTE: not sure whether better to do ones([1,3]) or ones((1,3)) in terms of readability
w = ones([1,3])    # 1x3 vector of ones - note that this could be ones(3), which in octave is a 3x3 matrix
w = zeros([1,3])
w = rand(1,3)  # drawn from a uniform distribution 
w = randn(1,3) # drawn from a normal distribution (mean=0, var=1)
w = -6 + sqrt(10)*randn(10000)  # (mean = 1, var = 2)
hist(w) # note that w needs to be a single dimension array like array([ 1.,  1.,  1.]) and not array([[ 1.,  1.,  1.]])
I = eye(4)    # 4x4 identity matrix

# help function
help(eye) # use q to get out of help mode
help(rand)

# =======================================================
# Section 2: Octave Tutorial: Moving data around 


## dimensions
sz = shape(A) # gives dimensions
size(A,0)  # number of rows
size(A,1)  # number of cols
max(shape(A))  # size of longest dimension
A.shape # tuple of dimensions OR shape(A)
A.ndim # number of dimensions OR ndim(A)



# show current directory (current path)
# %pwd #magic command for present working directory
# # %cd C:\Users\ang\Octave_files   # change directory 
ls     # list files in current directory 
q1y = loadtxt("priceY.dat") 
q1x = loadtxt("featuresX.dat") # need loadtxt to grab multiple columns
who()    # list *Numpy arrays* in given dictionary, if no dict given, shows
            # globals() [in IPython, this also shows all the `_` variables
# whos   # This is the equivalent of who in Octave
del q1y       # deletes the identifier from namespace (and if no other refs, deletes altogether)
v = q1x[0:10] # note this takes all columns, unlike Octave which defaults to take first
save("my_file", v) # saves as my_file.npy in binary format
# you can also save multiple with savez, load it with pickle and then access the arrays like a dictionary (see help(savez) for more)
savetxt("my_file.txt",v) # saves in textformat
# can also dump using the following but probably not so useful ...
#v.tofile("my_file.txt", ";", format="%0.2f") # save v as a csv-ish file HOWEVER note that this loses precision, and also the matrix structure ...
# defaults for tofile are sep="" (binary format) and format="%s"

## indexing
A[2,1]  # indexing is (row,col)
A[1,:]  # get the 2nd row. (0-indexed)
        # ":" means every element along that dimension
A[:,1]  # get the 2nd col
A[(0,2),:]

A[(0, 2), :] = 5 # set all of certain elements 'broadcast' value 
print A

A[:,1] = [10, 11, 12]     # change second column
A = hstack((A,vstack((1,2,3)))) # append column vec
A.ravel() # output all elements as a 1D matrix colum, but default iterating rows first, while Octave A(:) does columns first
A.flatten() # same as ravel as far as I can tell - pass order='F' as a parameter to get columns first
A.flat # iterator over elements of A

# Putting data together 
hstack([A, vstack((100, 101, 102))])
B = array([[11,12], [13, 14], [15, 16]]) # same dims as A
hstack([A, B]) # makes a 3 x 4 matrix
vstack([A,B]) # makes a 6 x 2 matrix


# =======================================================
# Section 3: Octave Tutorial: Computing on data 


## matrix operations
A * B # element-wise multiplication
A.dot(C) # matrix multiplication
matrix(A) * matrix(C) # matrix multiplication 
# discussion of array vs matrix in numpy http://www.scipy.org/NumPy_for_Matlab_Users/#head-e9a492daa18afcd86e84e07cd2824a9b1b651935
# A * C  or matrix(A) * matrix(B) gives error - wrong dimensions
A ** 2 # or power(A,2*ones(shape(A))) does equivalent of Octave .^ 2
v = array([[1],[2],[3]])
1. / v
log(v)  # functions like this operate element-wise on vecs or matrices 
exp(v)  # e^<element>
abs(v)  #
v == 1 # boolean array
v.all() # true iff every number > 0
v.any() # true iff *any* number > 0

-v  # -1*v

v + ones((shape(v))) # v + 1  # same

A.transpose()  # matrix transpose

## misc useful functions

# max  (or min)
a = array([1, 15, 2, 0.5])
val = a.max()
val,ind = a.max(0),a.argmax(0)
A.max(1) # print for each column
A.max(0) # print max for each row
a.min()
a.mean()

# find
a < 3
find(a < 3) # returns the indices where condition is true for the *flattened* matrix

from magic_square import *
A = magic(3) # magic square code here: http://pydoc.net/magic_square/
find(A>=7) # as noted above, get index for flattened matrix

# sum, prod
sum(a)
prod(a)
floor(a) # or ceil(a)
maximum(rand(3,3),rand(3,3))
[max(row) for row in A.transpose()] # not sure if we can go simpler - this is Octave target: max(A,[],1)
[max(row) for row in A] # not sure if we can go simpler - this is Octave target: min(A,[],2)
A = magic(9)

sum(A,0) # OR A.sum(0)
sum(A,1)
sum(sum(A * eye(9), 1)) 
sum( A * eye(9) ) # default is for sum to sum all items
sum( A * flipud(eye(9)))


# Matrix inverse (pseudo-inverse)
pinv(A)       # inv(A'*A)*A'


# =======================================================
# Section 4: Octave Tutorial: Plotting 


## plotting
t = linspace(0,0.98,99)
y1 = sin(2*pi*4*t)
plot(t,y1)
y2 = cos(2*pi*4*t)
plot(t,y2,'r')
xlabel('time')
ylabel('value')
legend(('sin','cos'))
title('my plot')
savefig('myplot.png') 
close()
# to get a new plot, call figure
fig2 = figure(); clf
subplot(1,2,1)  # Divide plot into 1x2 grid, access 1st element
plot(t,y1)
subplot(1,2,2)  # Divide plot into 1x2 grid, access 2nd element
plot(t,y2)
axis([0.5, 1, -1, 1])  # change axis scale

## display a matrix (or image)  # imshow not working for Sam on OSX 10.6.8 ...
fig3 = figure()
img = imshow(magic(15))
colorbar(img)
gray() # set the colormap to gray
fig4 = figure()
colorbar(imshow(magic(15), cmap=cm.hot)) # all in one line
print fig3
print fig4
# % comma-chaining function calls.  
a=1;b=2;c=3 # can use semicolon to do multiple statements on a single line, but it's unpythonic


# =======================================================
# Section 5: Octave Tutorial: For, while, if statements, and functions.

v = zeros([10,1])
for i in range(10): # note this runs from 0 to 9; python indices start at 0
    v[i] = 2**i
#Can also use "break" and "continue" inside for and while loops to control execution.

i = 0
while i <= 4:
  v[i] = 100
  i += 1

i = 0
while True: 
  v[i] = 999
  i += 1
  if i == 5:
    break

if v[1]==1:
  print('The value is one!') # Python 3 anyone?
elif v[1]==2:
  print('The value is two!')
else:
  print('The value is not one or two!')

# exit # to quit

# Functions

# Create a file called squareThisNumber.py with the following contents (without the #):

#def squareThisNumber(x):
#    r = x * x
#    return r

from squareThisNumber import *
squareThisNumber(5)

# If function is undefine, use "pwd" to check current directory (path), 
# and "%cd" to change directories

# not sure about addpath - got the whole pythonpath thing ...

# If you have defined other functions such as costFunctionJ, 
# the following code will work too. 

X = vstack(([1, 1], [1, 2], [1, 3]))
y = vstack((1,2,3))

theta = vstack((0,1))
from costFunctionJ import costFunctionJ
j = costFunctionJ(X, y, theta)

theta = vstack((0,0)) 
j = costFunctionJ(X, y, theta)

# ==============================================
# Saving your session
# You might want to save what you've done to run again in the future.  It's really easy to do, just type:

logstart "myfile.py"
# this will create a logfile called "myfile.py" in the current directory with all of your work
