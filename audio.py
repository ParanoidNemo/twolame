#! /usr/bin/env python

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

import os, sys
import alsaaudio

from spam import beshell
from spam import methods
from spam import volume

theme = beshell.Theme()

css = os.path.join(theme.path, 'style.css.d', 'tl_audio.css')
icon = os.path.join(theme.path, "TopPanel", "audio.png")

m = alsaaudio.Mixer()

vol_info = methods.create_dict(volume.alsa_info(m))
vol_info["{icon}"] = icon
vol_info["{x}"] = css
