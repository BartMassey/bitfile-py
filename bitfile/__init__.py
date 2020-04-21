"""
bitfile: A python I/O class for files containing arbitrary data sizes.
Copyright (C) 2010
      Michael Dipperstein (mdipperstein@gmail.com)

Bitfile is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the
Free Software Foundation; either version 3 of the License, or (at your
option) any later version.

Bitfile is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys

if sys.version_info < (3, 2):
    from bitfile import BitFile
else:
    from bitfile.bitfile import BitFile

__author__ = "Michael Dipperstein <mdipperstein@gmail.com>"
__license__ = "GPL"
__version__ = "0.3.1"
