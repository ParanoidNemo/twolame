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
import os, sys, re

#import downloaded module(s)
import musicpd

#import custom module(s)
import rc
from spam import beshell
from spam import music
from spam import methods

#gathering information(s)
rc_file = os.path.join(beshell.Theme.path(), 'twolamerc')

rc.get_rc(rc_file)

css = os.path.join(beshell.Theme.path(), 'style.css.d', rc.CSS)

c = musicpd.MPDClient()

info_pl = {}

play = os.path.join(beshell.Theme.path(), 'twolame', 'icons', 'play.png')
pause = os.path.join(beshell.Theme.path(), 'twolame', 'icons', 'pause.png')
stop = os.path.join(beshell.Theme.path(), 'twolame', 'icons', 'stop.png')

panel = os.path.join(beshell.Theme.path(), 'twolame', 'icons', 'down.png')

info = methods.create_dict(music.process_mpd(c))
info['{x}'] = css

if c.status()['state'] == 'play':
    toggle = pause
elif c.status()['state'] == 'pause':
    toggle = play
else:
    toggle = stop

info['{button}'] = toggle
info['{dot}'] = panel

pl = ''
for item in music.playlist(c):
    pl += item

info_pl = {'{playlist}': pl, '{x}': css}

info_cv = methods.create_dict(music.process_mpd(c))
info_cv["{cover}"] = music.cover(rc.COVER_PATH, c)
info_cv["{x}"] = css
