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

from spam import beshell
from spam import network

theme = beshell.Theme()
# define interface
interface = "wlp3s0"

net = {"interface": interface}

if network.wifi_info(interface)[1] == "off/any":
    net["{connection}"] = "off"
    net["{quality}"] = "n/a"
    net["{essid}"] = "n/a"
else:
    net["{connection}"] = "on"
    net["{quality}"] = network.wifi_info(interface)[2]
    net["{essid}"] = network.wifi_info(interface)[1]

css = os.path.join(theme.path, "style.css.d", "tl_net")
icon = os.path.join(theme.path, "TopPanel", "net.png")

net["{icon}"] = icon
net["{x}"] = css
