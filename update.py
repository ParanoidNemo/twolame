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

rc_file = os.path.join(beshell.Theme.path(), 'twolamerc')

rc.get_rc(rc_file)

distro = check.distro()

if distro == 'debian':
    up_check_apt = subprocess.run(['aptitude', 'search', '"~U"'], stdout=subprocess.PIPE, universal_newlines=True)
    up_check = up_check_apt.stdout
elif distro == 'fedora':
    up_check_dnf = subprocess.run(['dnf', 'check-update'], stdout=subprocess.PIPE, universal_newlines=True)
    up_check = up_check_dnf.stdout
elif distro == 'archlinux':
    up_check_repo = subprocess.run(['checkupdates'], stdout=subprocess.PIPE, universal_newlines=True)
    up_check_aur = subprocess.run(['cower', '--color=never', '-uq'], stdout=subprocess.PIPE, universal_newlines=True)
    up_check = up_check_repo.stdout + up_check_aur.stdout

update = []

for line in up_check.split():
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