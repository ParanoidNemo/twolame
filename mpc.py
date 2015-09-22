#!/usr/bin/env python

#   Copyright (C) 2015 by Andrea Calzavacca <paranoid.nemo@gmail.com>
#
#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the
#   Free Software Foundation, Inc.,
#   59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

#import std module(s)
import os, sys

#import custom module(s)
from spam import beshell
from spam import musicinfo

#gathering information(s)

#define run function
def run():
    global format_string
    if not os.path.isdir(os.path.expanduser('~/.local/share/be.shell/fifo')):
        os.makedirs(os.path.expanduser('~/.local/share/be.shell/fifo'))
    try:
        os.mkfifo(os.path.expanduser('~/.local/share/be.shell/fifo/mpd'))
    except:
        pass

#add info to fifo

#-------------------------------------------------------------------------------
#------------------------------DA CONTROLLARE-----------------------------------
#-------------------------------------------------------------------------------
with open(os.path.expanduser('~/.config/skutter/mpd.format')) as f:
    for line in f:
        if line.startswith('#'):
            continue
        self.format_string += line

self.format_string = re.sub(r'>\s+<', '><', self.format_string)
