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

import os, sys, re
import configparser

import rc
from spam import clouds
from spam import beshell
from spam import methods

rc_file = os.path.join(beshell.Theme.path(), 'twolamerc')
format_file = os.path.join(beshell.Theme.path(), 'twolame', 'cloud_one.format')

rc.get_rc(rc_file)

css = os.path.join(beshell.Theme.path(), 'style.css.d', rc.CSS)

cloud_info = []

if rc.RCLONE == '1':

    parser = configparser.ConfigParser()
    rclone_cfg = rc.RCLONE_CONFIG_FILE
    read_cfg = parser.read(rclone_cfg)

    services_list = []

    for item in parser.sections():
        service = parser.get(item, 'type')
        l = clouds.Rclone.space_info(item, service)
        d = methods.create_dict(l)
        outstring = methods.insert_data(methods.format_string(format_file), d)
        cloud_info.append(outstring)

if rc.MEGA == '1':

    l = clouds.Mega.space_info(rc.SIZE)
    d = methods.create_dict(l)
    outstring = methods.insert_data(methods.format_string(format_file), d)
    cloud_info.append(outstring)

info = methods.create_dict(cloud_info)
info['{x}'] = css
