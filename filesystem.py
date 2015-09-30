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
import rc

rc_file = os.path.join(beshell.Theme.path(), 'twolamerc')

rc.get_rc(rc_file)

mnt1 = os.path.expanduser(rc.MNT1)
mnt2 = os.path.expanduser(rc.MNT2)
css = os.path.join(beshell.Theme.path(), 'style.css.d', rc.CSS)

info = { '{0}': fs.fs_info(mnt1)['mount'], '{1}': fs.fs_info(mnt1)['free'], '{2}': fs.fs_info(mnt1)['tot'], '{3}': fs.fs_info(mnt1)['used'], '{4}': fs.fs_info(mnt1)['pfree'], '{5}': fs.fs_info(mnt1)['pused'], '{6}': fs.fs_info(mnt2)['mount'], '{7}': fs.fs_info(mnt2)['free'], '{8}': fs.fs_info(mnt2)['tot'], '{9}': fs.fs_info(mnt2)['used'], '{10}': fs.fs_info(mnt2)['pfree'], '{11}': fs.fs_info(mnt2)['pused'], '{x}': css }
