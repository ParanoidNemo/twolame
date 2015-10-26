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

import os
from spam import fs
from spam import beshell
from spam import methods
import rc

rc_file = os.path.join(beshell.Theme.path(), 'twolamerc')

rc.get_rc(rc_file)

dev = []

try:
    mnt0 = os.path.expanduser(rc.MNT[0])
    dev.append(mnt0)
    mnt1 = os.path.expanduser(rc.MNT[1])
    dev.append(mnt1)
    mnt2 = os.path.expanduser(rc.MNT[2])
    dev.append(mnt2)
    mnt3 = os.path.expanduser(rc.MNT[3])
    dev.append(mnt3)
    mnt4 = os.path.expanduser(rc.MNT[4])
    dev.append(mnt4)
except IndexError:
    pass
except Exception:
    raise

css = os.path.join(beshell.Theme.path(), 'style.css.d', rc.CSS)
fm = rc.FM
info = []
_info = {}

for item in dev:
    info.append(fs.fs_info(item)['mount'])
    info.append(fs.fs_info(item)['free'])
    info.append(fs.fs_info(item)['tot'])
    info.append(fs.fs_info(item)['used'])
    info.append(fs.fs_info(item)['pfree'])
    info.append(fs.fs_info(item)['pused'])

_info = methods.create_dict(info)
_info['{x}'] = css
_info['{e}'] = fm
