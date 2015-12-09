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
import rc

from spam import system_info
from spam import beshell
from spam import methods

theme = beshell.Theme()
rc_file = os.path.join(theme.path, 'twolamerc')

rc.get_rc(rc_file)

css = os.path.join(theme.path, 'style.css.d', 'tl_system.css')
fm = rc.FM
pm = rc.PM

si = []

#-------------------------- format file definition------------------------------

fs_format_file = os.path.join(theme.path, 'twolame', 'fs.format')

#------------------------------collecting info----------------------------------

# distro info
ds = system_info.distro()

# de info
de = system_info.de()

# wm info
wm = system_info.wm()

# uptime info
ut = system_info.uptime()

# machine info
mi = system_info.machine()

# cpu info
cpu = system_info.cpu()

# ram info
ram = system_info.ram()

# update info
update = system_info.update(pm)

# fs info
for item in rc.MNT.split(','):

    l = system_info.fs(item)
    o = methods.create_dict(l)
    out = methods.insert_data(methods.format_string(fs_format_file), o)

    si.append(out)
#--------------------------------popolate dict----------------------------------

si_dict = methods.create_dict(si)
si_dict["{distro}"] = ds
si_dict["{de}"] = de
si_dict["{wm}"] = wm
si_dict["{ut_days}"] = str(ut[0])
si_dict["{ut_hours}"] = str(ut[1])
si_dict["{ut_minutes}"] = str(ut[2])
si_dict["{ut_seconds}"] = str(ut[3])
si_dict["{hostname}"] = mi[1]
si_dict["{kernel_build}"] = mi[2]
si_dict["{architecture}"] = mi[4]
si_dict["{cpu}"] = cpu
si_dict["{ram_tot}"] = ram[1]
si_dict["{ram_used}"] = ram[2]
si_dict["{ram_free}"] = ram[6]
si_dict["{ram_used_perc}"] = ram[7]
si_dict["{ram_free_perc}"] = ram[8]
si_dict["{x}"] = css
si_dict["{e}"] = fm
si_dict["{updates}"] = update[0]
try:
    si_dict["{aur}"] = update[1]
except Exception:
    pass
