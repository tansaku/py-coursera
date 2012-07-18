py-coursera
===========

Python framework for Coursera [PGM](https://www.coursera.org/course/pgm) and
[ML](https://www.coursera.org/course/ml) homeworks

The Coursera PGM and ML classes use [Octave](http://www.gnu.org/software/octave/) 
for their homework assignments.Arguably Octave is great for novice students
getting started quickly with a single package that allows them to quickly
manipulate matrices etc.  However many students in the PGM and ML courses
have wondered if there couldn't be a Python alternative based on
[SciPy](http://www.scipy.org/) or other similar frameworks for Python.

While it may not be possible to create a perfect replacement for Octave many
more programming experienced students would love to be working with Python
rather than Octave, particularly because of support for testing, continuous
integration and so forth.

This repository is a placeholder for any and all attempts to replicate parts of
the Coursera PGM and ML homework assignment code in Python.  It was created as
part of [this discussion][OrigDisc]
in the PGM class, which annoyingly you will be unable to access if you didn't
sign up for PGM first time around, so please contact
[sjoseph@hpu.edu](mailto:sjoseph@hpu.edu) for a summary if you're interested.

In the first instance we'll attempt to recreate the ML/PGM Octave tutorials
using the Enthought SciPy/Python distribution.  Here's the start of a
transcript based on Prof Ng's [Octave transcript][OctaveTrans]

[ipython session (sort of)](https://github.com/tansaku/py-coursera/blob/master/ipython_session.py)

Let me elaborate, [IPython](http://ipython.org) is Python with a high powered interactive shell:

[http://ipython.org/](http://ipython.org/)

which we've pulled in as part of the one click install [Enthought distribution.](http://www.enthought.com),

[http://www.enthought.com/](http://www.enthought.com/)

This [ipython_session][IPSession] thing is unfortunately incomplete at present
:-(  We've just got started and have only finished translating the first couple
of sections.  Note the change from python to Octave comments.

The rest is TODO - We'll keep working on it, but all help appreciated it.
Please let us know your github id if you'd like to collaborate. Feel free to
email [sjoseph@hpu.edu](mailto:sjoseph@hpu.edu).

[OctaveTrans]: http://spark-university.s3.amazonaws.com/stanford-pgm/slides/octave_session.m
[IPSession]: https://github.com/tansaku/py-coursera/blob/master/ipython_session.py
[OrigDisc]: https://class.coursera.org/pgm/forum/thread?thread_id=2382

Many thanks to all Contributors including [Jeff Tratner](https://github.com/jtratner), Arthur Dent, Andrew Clegg
