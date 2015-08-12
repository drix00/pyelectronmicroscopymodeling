#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2011 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision$"
__svnDate__ = "$Date$"
__svnId__ = "$Id$"

# Standard library modules.

# Third party modules.
try:
    from OpenGL.GL import *
    from OpenGL.GLUT import *
    haveOpenGL = True
except ImportError:
    haveOpenGL = False

# Local modules.

# Project modules

# Globals and constants variables.

def runViewer():
    pass

if __name__ == '__main__':  #pragma: no cover
    runViewer()
