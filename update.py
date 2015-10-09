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

import os, sys
import subprocess

import rc
from spam import check
from spam import beshell

distro = check.distro()

if distro == 'debian':
    up_check = subprocess.check_call(['aptitude', 'search', '"~U"'])
elif distro == 'fedora':
    up_check = subprocess.check_call(['dnf', 'check-update'])
elif distro == 'archlinux':
    up_check = subprocess.run(['checkupdates'], stdout=subprocess.PIPE, universal_newlines=True)
    #up_check_aur = subprocess.check_call(['pacaur', '-k'])

update = []

for line in up_check.stdout.split():
    if line.startswith('error'):
        pass
    else:
        update.append(line)

css = os.path.join(beshell.Theme.path(), 'style.css.d', rc.CSS)
_update = {}
tot = len(update)

if len(update) < 10:
    nl = 10 - tot
    for l in range(nl):
        update.append('')
else:
    pass

for index, item in enumerate(update[-10:]):
    i = '{' + str(index) + '}'
    _update[i] = item
_update['{x}'] = css
_update['{tot}'] = str(tot)
