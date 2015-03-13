pymanymouse: a portable library to allow input from multiple mice

Authors
=======

* Nick Irvine <nfirvine@nfirvine.com>

About
=====

pymanymouse is a wrapper around the C ManyMouse library made by Ryan Gordon.
The original can be found at http://icculus.org/manymouse

Dependencies
============

* svn (for downloading ManyMouse the original)
* gcc, make, standard c libs, etc.
* python header files (Python.h)
* swig

Building
========

To build, run `build.sh`. This will:
1. download the proper revision of manymouse from svn
2. build manymouse
3. build pymanymouse

Using
=====

The interface to manymouse (C) is pretty thin: it's still rife with gross
C-ness.  The only difference between the API is that for pymanymouse,
you:
import manymouse
manymouse.some_function()

as opposed to the ManyMouse_SomeFunction().

See test_manymouse_sdl.py for an example.

Also provided is manymouse_pygame.py, a small library that bridges manymouse and pygame by loading manymouse events into the pygame event queue.

Licence
=======

ManyMouse's original licence is zlib, which can be found in the LICENSE file that comes with it (or after the build.sh script is run).  pymanymouse's licence is GPLv3, which can be found at http://www.gnu.org/licences/gpl.txt
