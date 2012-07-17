py-coursera
===========

Python framework for Coursera [PGM](https://www.coursera.org/course/pgm) and [ML](https://www.coursera.org/course/ml) homeworks

The Coursera PGM and ML classes use [Octave](http://www.gnu.org/software/octave/) for their homework assignments.  Arguably Octave is great for novice students getting started quickly with a single package that allows them to quickly manipulate matrices etc.  However many students in the PGM and ML courses have wondered if there couldn't be a Python alternative based on [SciPy](http://www.scipy.org/) or other similar frameworks for Python.

While it may not be possible to create a perfect replacement for Octave many more programming experienced students would love to be working with Python rather than Octave, particularly because of support for testing, continuous integration and so forth.

This repository is a placeholder for any and all attempts to replicate parts of the Coursera PGM and ML homework assignment code in Python.

In the first instance we'll attempt to recreate the ML/PGM Octave tutorials using the Enthought SciPy/Python distribution.  Here's the start of a transcript based on Prof Ng's [Octave transcript](http://spark-university.s3.amazonaws.com/stanford-pgm/slides/octave_session.m)

In [2]: 5+6
Out[2]: 11

In [3]: 3-2
Out[3]: 1

In [4]: 5*8
Out[4]: 40

In [5]: 1/2
Out[5]: 0

In [6]: 1/2.
Out[6]: 0.5

In [7]: 2^6
Out[7]: 4

In [8]: 2**6
Out[8]: 64

In [9]: 1 == 2
Out[9]: False

In [10]: 1 != 2
Out[10]: True

In [11]: 1 && 0
  File "<ipython-input-11-50139b8f39e2>", line 1
    1 && 0
       ^
SyntaxError: invalid syntax


In [12]: 1 ^ 0
Out[12]: 1

In [13]: 1 | 0
Out[13]: 1

In [14]: 1 and 0
Out[14]: 0

In [15]: 1 or 0
Out[15]: 1

In [16]: 1 xor 0
  File "<ipython-input-16-50393c29d02c>", line 1
    1 xor 0
        ^
SyntaxError: invalid syntax


In [17]: xor(1,0)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/Users/samueljoseph/<ipython-input-17-0c49018d60ba> in <module>()
----> 1 xor(1,0)

NameError: name 'xor' is not defined

In [18]: 1 ^ 0
Out[18]: 1

In [19]: 1 ^ 1
Out[19]: 0

In [20]: 

In [20]: 0 ^ 0
Out[20]: 0

In [21]: 
